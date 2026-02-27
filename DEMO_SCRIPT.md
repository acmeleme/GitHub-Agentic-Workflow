# GitHub Agentic Workflow Demo Script

Use this script to present the Architect → Developer → QA workflow in 8–10 minutes.

## 0) Setup (before audience joins)

1. Open repository: https://github.com/acmeleme/GitHub-Agentic-Workflow
2. Confirm Actions tab is enabled.
3. Run workflow **Bootstrap Demo Labels** once (if not done yet).
4. Keep two tabs ready:
   - **Issues**
   - **Actions**

## 1) Opening (30 seconds)

"This demo shows a GitHub Agentic Workflow with three roles: Architect, Developer, and QA.  
The workflow can start from an issue or manually, and every stage posts artifacts and status updates for full traceability."

## 2) Trigger by issue (2 minutes)

1. Go to **Issues** → **New issue**.
2. Select template **Agentic Demo Request**.
3. Fill example:
   - Problem statement: "Create a small web app with a health endpoint and README updates."
   - Acceptance criteria: 3 bullet points.
   - Priority: Medium.
4. Submit issue.
5. Confirm label **agentic-demo** is present.

Talk track:
"This label is the trigger contract. Once present, the workflow starts automatically."

## 3) Watch execution (3 minutes)

1. Open **Actions** → **GitHub Agentic Workflow Demo** run.
2. Show job order:
   - Intake
   - Architect
   - Developer
   - QA
   - Summary
3. Open issue comments and refresh.

Talk track:
"Each role emits a structured handoff, and now the Developer stage also creates real code and opens a pull request."

## 4) Show artifacts (2 minutes)

In the workflow run, open artifacts and show:
- architect-report
- developer-report
- qa-report
- execution-summary

Also open the PR link posted by Developer and show generated files:
- generated-app/app.py
- generated-app/requirements.txt
- generated-app/README.md

Talk track:
"This demo now creates real code and a real PR. The architecture still stays role-based and traceable end-to-end."

## 5) Manual trigger fallback (1 minute)

1. In **Actions**, open **GitHub Agentic Workflow Demo**.
2. Click **Run workflow**.
3. Enter:
   - feature_summary: "Build a basic TODO app with tests"
   - priority: high
4. Start run and show same lifecycle.

Talk track:
"Manual dispatch supports operations teams and demos when issue intake is not desired."

## 6) Close (30 seconds)

"We demonstrated deterministic multi-role orchestration on GitHub-native primitives: issues, actions, comments, and artifacts.  
Next step is replacing deterministic code generation with model-driven implementation while preserving governance and traceability."

## Optional Q&A Answers

- **Do we need secrets now?**
  - Not for current mocked flow. It uses GitHub Actions token permissions.
- **Can this create real code PRs?**
  - Yes. Replace Developer stage with real coding agent actions and PR creation.
- **Can we add approval gates?**
  - Yes. Add environment protection or required reviewers before merge.
