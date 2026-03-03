from flask import Flask, redirect, render_template_string, request, session, url_for
import random

app = Flask(__name__)
app.secret_key = "agentic-demo-hangman-secret"

WORDS = ["BRASILIA", "SALVADOR", "RECIFE", "MANAUS", "CURITIBA"]
MAX_ERRORS = 6

PAGE = """
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Jogo da Forca - Capitais Brasileiras</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; color: #1f2937; }
      .card { max-width: 640px; padding: 1.25rem; border: 1px solid #e5e7eb; border-radius: 10px; }
      .word { font-size: 2rem; letter-spacing: 0.4rem; margin: 1rem 0; font-weight: bold; }
      .status { margin: 0.6rem 0; }
      .ok { color: #065f46; }
      .fail { color: #991b1b; }
      input { font-size: 1rem; width: 3rem; text-align: center; text-transform: uppercase; }
      button { margin-left: 0.5rem; }
      .meta { color: #4b5563; font-size: 0.95rem; }
      .letters { margin-top: 0.7rem; }
    </style>
  </head>
  <body>
    <div class="card">
      <h1>Jogo da Forca</h1>
      <p class="meta">Tema: capitais brasileiras (5 palavras fixas)</p>

      <div class="word">{{ masked_word }}</div>
      <div class="status">Tentativas restantes: <strong>{{ remaining }}</strong></div>
      <div class="letters">Letras usadas: {{ used_letters or "(nenhuma)" }}</div>

      {% if won %}
        <p class="status ok"><strong>Você venceu!</strong> A palavra era {{ word }}.</p>
      {% elif lost %}
        <p class="status fail"><strong>Você perdeu!</strong> A palavra era {{ word }}.</p>
      {% endif %}

      {% if not won and not lost %}
        <form method="post" action="{{ url_for('guess') }}">
          <label for="letter">Letra:</label>
          <input id="letter" name="letter" maxlength="1" required autofocus />
          <button type="submit">Tentar</button>
        </form>
      {% endif %}

      <form method="post" action="{{ url_for('reset') }}" style="margin-top: 0.9rem;">
        <button type="submit">Reiniciar jogo</button>
      </form>
    </div>
  </body>
</html>
"""


def start_new_game():
    session["word"] = random.choice(WORDS)
    session["used_letters"] = []
    session["errors"] = 0


def current_state():
    if "word" not in session:
        start_new_game()

    word = session["word"]
    used_letters = session.get("used_letters", [])
    errors = int(session.get("errors", 0))

    masked_word = " ".join([char if char in used_letters else "_" for char in word])
    won = all(char in used_letters for char in word)
    lost = errors >= MAX_ERRORS
    remaining = MAX_ERRORS - errors

    return {
        "word": word,
        "masked_word": masked_word,
        "used_letters": " ".join(used_letters),
        "won": won,
        "lost": lost,
        "remaining": remaining,
    }


@app.get("/")
def index():
    return render_template_string(PAGE, **current_state())


@app.post("/guess")
def guess():
    state = current_state()
    if state["won"] or state["lost"]:
        return redirect(url_for("index"))

    letter = (request.form.get("letter", "").strip().upper())[:1]
    if not letter or not letter.isalpha():
        return redirect(url_for("index"))

    used_letters = session.get("used_letters", [])
    if letter in used_letters:
        return redirect(url_for("index"))

    used_letters.append(letter)
    session["used_letters"] = used_letters

    if letter not in session["word"]:
        session["errors"] = int(session.get("errors", 0)) + 1

    return redirect(url_for("index"))


@app.post("/reset")
def reset():
    start_new_game()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
