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
- `DEMO_SCRIPT.md` presenter script and talk track

## Quick Start
Follow this as if you are running GitHub Actions for the first time.

### Step 1: Open the repository in GitHub
1. Open your browser and go to this repo.
2. Click the **Actions** tab.
3. If GitHub asks to enable workflows, click **Enable workflows**.

Expected result:
- You can see the workflow list on the left side.

### Step 2: Create required labels (one-time setup)
1. In **Actions**, click workflow **Bootstrap Demo Labels**.
2. Click **Run workflow** (top-right) and confirm.
3. Wait until it shows a green check mark.

Expected result:
- Labels are created: `agentic-demo`, `needs-architect`, `needs-dev`, `needs-qa`.

### Step 3: Trigger demo from an issue (recommended)
1. Go to **Issues** tab.
2. Click **New issue**.
3. Choose template **Agentic Demo Request**.
4. Fill the form (problem, acceptance criteria, priority).
5. Submit the issue.
6. Confirm the issue has label `agentic-demo`.

Expected result:
- A new run starts in **Actions** for workflow **GitHub Agentic Workflow Demo**.

### Step 4: Watch the workflow stages
1. Open the running workflow.
2. Confirm jobs execute in this sequence:
   1. Intake
   2. Architect
   3. Developer
   4. QA
   5. Summary

Expected result:
- Each stage finishes with success (green check).

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
- You can see full handoff history from Architect → Developer → QA.

### Step 6: Manual trigger (fallback option)
If issue flow is not available, run manually:
1. Go to **Actions** → **GitHub Agentic Workflow Demo**.
2. Click **Run workflow**.
3. Fill `feature_summary` and `priority`.
4. Click **Run workflow**.

Expected result:
- Same lifecycle runs even without creating an issue.

## Trigger Rules
- Issue trigger runs when event is `opened`, `edited`, or `labeled` and issue has label `agentic-demo` **or** title starts with `[Agentic Demo]`.
- Manual trigger always runs.

## Notes
- Current implementation is a production-like orchestration demo with mocked role outputs.
- To make roles truly autonomous, replace role report generation steps with your preferred coding/AI actions while preserving output contracts.

## Troubleshooting
- No workflow run after creating an issue:
   - Ensure the issue has label `agentic-demo` or title starts with `[Agentic Demo]`.
- Intake ran but Architect/Developer/QA were skipped:
   - Check the issue comment from Intake for the skip reason.
- Labels are missing:
   - Run workflow **Bootstrap Demo Labels** once from the Actions tab.
- Manual run failed to attach issue comments:
   - Provide `issue_number` in manual trigger input if you want comments posted to an issue.
