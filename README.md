# GitHub Agentic Workflow Demo

Demo repository for a role-based GitHub workflow with three agents:

The pipeline can run from:
1. Issue events (issue has `agentic-demo` label)
2. Manual trigger (`workflow_dispatch`)

## Included Files

## Quick Start
Follow this as if you are running GitHub Actions for the first time.

### Step 1: Open the repository in GitHub
1. Open your browser and go to this repo.
2. Click the **Actions** tab.
3. If GitHub asks to enable workflows, click **Enable workflows**.

Expected result:

### Step 2: Create required labels (one-time setup)
1. In **Actions**, click workflow **Bootstrap Demo Labels**.
2. Click **Run workflow** (top-right) and confirm.
3. Wait until it shows a green check mark.

Expected result:

### Step 3: Trigger demo from an issue (recommended)
1. Go to **Issues** tab.
2. Click **New issue**.
3. Choose template **Agentic Demo Request**.
4. Fill the form (problem, acceptance criteria, priority).
5. Submit the issue.
6. Confirm the issue has label `agentic-demo`.

Expected result:

### Step 4: Watch the workflow stages
1. Open the running workflow.
2. Confirm jobs execute in this sequence:
   1. Intake
   2. Architect
   3. Developer
   4. QA
   5. Summary

Expected result:

### Step 5: Validate outputs
1. Open the issue you created.
2. Refresh and check bot comments for stage progress.
3. In the workflow run, open **Artifacts**.
4. Download and inspect:
   - `architect-report`
   - `developer-report`
   - `qa-report`
   - `execution-summary`

Expected result:

### Step 6: Manual trigger (fallback option)
If issue flow is not available, run manually:
1. Go to **Actions** → **GitHub Agentic Workflow Demo**.
2. Click **Run workflow**.
3. Fill `feature_summary` and `priority`.
4. Click **Run workflow**.

Expected result:

## Trigger Rules
   - `opened` or `edited` and issue has label `agentic-demo` **or** title starts with `[Agentic Demo]`.
   - `labeled` only when the label added is `agentic-demo`.

## Notes

## Troubleshooting
   - Ensure the issue has label `agentic-demo` or title starts with `[Agentic Demo]`.
   - Check the issue comment from Intake for the skip reason.
   - Run workflow **Bootstrap Demo Labels** once from the Actions tab.
   - Provide `issue_number` in manual trigger input if you want comments posted to an issue.
   - Your org/repo policy may block GitHub Actions from opening PRs automatically.
   - Use the provided `pull/new/...` URL to create the PR manually.
# GitHub Agentic Workflow Demo

## Overview
This workflow automates code generation from GitHub issues using the GitHub Copilot agent. When an issue is opened or labeled for agentic processing, the workflow extracts the request, generates code using Copilot, and creates a pull request with the generated code.

## Workflow Stages

1. **Intake**: Extracts the issue request and sets up tracking.
2. **Architect**: Normalizes the request and proposes a solution.
3. **Developer**: Uses GitHub Copilot SDK to generate code based on the issue request, commits the code, and opens a PR.
4. **QA**: Validates the generated code and posts results.
5. **Summary**: Posts a final execution summary to the issue.

## Developer Stage Details
- Installs Copilot SDK (`@github/copilot-sdk`).
- Authenticates using `GITHUB_TOKEN`.
- Calls Copilot agent with the normalized request.
- Saves generated code to `generated-app/app.py` and metadata to `.generated-run.txt`.
- Creates a branch and opens a PR.

## Requirements
- GitHub Copilot SDK access.
- `GITHUB_TOKEN` secret set in repository.
- Node.js 20+ for Developer job.

## Example Issue Flow
1. Open a new issue describing the code you want.
2. Add the `agentic-demo` label or use the `[Agentic Demo]` prefix in the title.
3. The workflow will:
   - Extract your request
   - Generate code using Copilot
   - Open a PR with the generated code
   - Post status updates and artifacts to the issue

## References
- [GitHub Copilot SDK](https://github.com/github/copilot-sdk)
- [Workflow YAML](.github/workflows/agentic-demo.yml)
