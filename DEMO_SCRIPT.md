
# Agentic Workflow Demo Script

## Purpose
Demonstrate end-to-end agentic code generation from GitHub issues using the Copilot agent.

## Steps

1. **Open an Issue**
   - Title: `[Agentic Demo] Create a REST API for books`
   - Body: "Please generate a Python Flask REST API with endpoints for CRUD operations on books."
   - Add label: `agentic-demo`

2. **Workflow Trigger**
   - Workflow starts automatically on issue creation or labeling.

3. **Intake Stage**
   - Extracts issue request and sets up tracking.
   - Posts status comment to issue.

4. **Architect Stage**
   - Normalizes request and proposes solution.
   - Posts architect report as artifact and comment.

5. **Developer Stage**
   - Installs Copilot SDK.
   - Authenticates with `GITHUB_TOKEN`.
   - Calls Copilot agent with request.
   - Saves generated code to `generated-app/app.py`.
   - Commits code, creates branch, opens PR.
   - Posts developer report and PR link to issue.

6. **QA Stage**
   - Validates generated code (mocked for demo).
   - Posts QA report to issue.

7. **Summary Stage**
   - Posts execution summary to issue.

## Expected Outcome
- PR is created with generated code.
- Issue receives status updates and artifacts.
- All stages are traceable via comments and artifacts.

## References
- [Workflow YAML](.github/workflows/agentic-demo.yml)
- [GitHub Copilot SDK](https://github.com/github/copilot-sdk)
