# GitHub Agentic Workflow Demo

Demo repository for a role-based GitHub workflow with three agents:
- Architect
- Developer
- QA

The pipeline can run from:
1. Issue events (issue has `agentic-demo` label)
2. Manual trigger (`workflow_dispatch`)

## Included Files
- `.github/workflows/agentic-demo.yml` main role workflow
- `.github/workflows/bootstrap-labels.yml` creates required labels
- `.github/ISSUE_TEMPLATE/agentic-demo.yml` request template
- `.github/agent-prompts/*.md` role prompt contracts

## Quick Start
1. Push this repository to GitHub.
2. Run workflow: **Bootstrap Demo Labels** once.
3. Create an issue from **Agentic Demo Request** template, or run **GitHub Agentic Workflow Demo** manually.
4. Follow issue comments and action artifacts:
   - `architect-report`
   - `developer-report`
   - `qa-report`
   - `execution-summary`

## Trigger Rules
- Issue trigger runs when event is `opened`, `edited`, or `labeled` **and** issue contains label `agentic-demo`.
- Manual trigger always runs.

## Notes
- Current implementation is a production-like orchestration demo with mocked role outputs.
- To make roles truly autonomous, replace role report generation steps with your preferred coding/AI actions while preserving output contracts.
