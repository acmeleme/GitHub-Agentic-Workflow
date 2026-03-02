# Roteiro de Demo para Cliente — GitHub Agentic Workflow

Use este roteiro para apresentar o fluxo Architect → Developer → QA em 10–12 minutos, com entrega final de um jogo da forca usando 5 capitais brasileiras.

## Objetivo da demo

Mostrar que um pedido de negócio vira execução rastreável no GitHub (Issue → Workflow → PR), com artefatos por papel e resultado final validável.

## Pré-requisito técnico importante

No estado atual deste repositório, a etapa Developer gera um app Flask básico de health check.
Para esta demo específica da forca, garanta antes da reunião que a etapa Developer esteja configurada para implementar o jogo solicitado.

## Escopo funcional a ser pedido na demo

Jogo da forca com palavras sorteadas entre estas 5 capitais:
- BRASILIA
- SALVADOR
- RECIFE
- MANAUS
- CURITIBA

## 0) Pré-demo (antes da reunião)

1. Abra o repositório: https://github.com/acmeleme/GitHub-Agentic-Workflow
2. Confirme que a aba **Actions** está habilitada.
3. Rode uma vez o workflow **Bootstrap Demo Labels** (setup inicial de labels).
4. Deixe 3 abas prontas:
   - **Issues**
   - **Actions**
   - **Pull requests**

Fala sugerida:
"Hoje vamos mostrar um fluxo agentic com governança: cada etapa registra decisão, implementação e validação antes da entrega final."

## 1) Abrir a demanda no Issue (2 minutos)

1. Vá em **Issues** → **New issue**.
2. Escolha o template **Agentic Demo Request**.
3. Preencha assim:
   - **Problem statement**: "Criar um jogo da forca web com 5 capitais brasileiras."
   - **Acceptance criteria**:
     - O jogo sorteia uma palavra entre BRASILIA, SALVADOR, RECIFE, MANAUS e CURITIBA.
     - O usuário pode tentar letras e ver acertos/erros.
     - O jogo indica vitória/derrota e permite reiniciar.
   - **Priority**: `high`
4. Submeta a issue.
5. Confirme que a label **agentic-demo** está presente.

Fala sugerida:
"A label é o contrato de automação. A partir daqui, o workflow inicia sem ação manual."

## 2) Acompanhar execução no Actions (3 minutos)

1. Abra **Actions** → execução de **GitHub Agentic Workflow Demo**.
2. Mostre a ordem dos jobs:
   - Intake
   - Architect
   - Developer
   - QA
   - Summary
3. Volte na issue e atualize os comentários para mostrar status em tempo real.

Fala sugerida:
"Cada papel entrega um handoff rastreável, permitindo auditoria e colaboração sem perder contexto."

## 3) Mostrar artefatos por papel (2 minutos)

No run do workflow, em **Artifacts**, abra:
- `architect-report`
- `developer-report`
- `qa-report`
- `execution-summary`

Pontos para destacar:
- O Architect transforma o pedido em plano e critérios.
- O Developer registra implementação e status do PR.
- O QA registra recomendação final.

## 4) Mostrar o PR da entrega (2 minutos)

1. Abra o link de PR comentado pelo Developer.
2. Mostre os arquivos gerados/alterados do app.
3. Destaque no diff onde está a lógica do jogo da forca e a lista das 5 capitais.

Fala sugerida:
"Aqui está a entrega técnica conectada ao pedido original, com trilha completa de decisão e validação."

## 5) Validação rápida do resultado (2–3 minutos)

No branch do PR (ou localmente), execute a aplicação e faça um teste curto:

1. Instale dependências.
2. Suba a aplicação.
3. Faça jogadas até ganhar/perder e depois reinicie.
4. Mostre que as palavras possíveis são apenas as 5 capitais definidas.

Checklist de aceite ao vivo:
- Sorteio restrito às 5 capitais.
- Entrada de letras funcionando.
- Estado de vitória/derrota visível.
- Reinício funcionando.

## 6) Encerramento (30–45 segundos)

Mensagem final sugerida:
"Em poucos minutos, vimos o ciclo completo: demanda, arquitetura, implementação, QA e evidências. O valor aqui é velocidade com governança e rastreabilidade nativas no GitHub."

## Plano B (se o trigger por issue falhar)

1. Vá em **Actions** → **GitHub Agentic Workflow Demo** → **Run workflow**.
2. Use em `feature_summary` o mesmo texto da demanda da forca.
3. Se quiser comentários na issue, informe `issue_number`.

## Q&A rápido (respostas prontas)

- **"Isso precisa de segredo extra?"**
  - Para este fluxo demo, não. O `GITHUB_TOKEN` com permissões do workflow é suficiente.
- **"Dá para incluir aprovação humana antes de merge?"**
  - Sim, com branch protection e required reviewers.
- **"Dá para trocar a implementação mock por agente real de código?"**
  - Sim, mantendo o mesmo contrato de handoff por etapa.
