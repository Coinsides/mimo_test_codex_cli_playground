# mimo_test_codex_cli_playground

A minimal sandbox repo to run the **Codex CLI Thread Playbook** end-to-end:

- TaskSpec (input) → `codex exec` (work) → tests/validation → TaskResult (output)
- Keep the workflow reproducible and reviewable.

## Quick start

1) Create a virtualenv and install deps:

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\pip install -r requirements.txt
```

2) Run tests:

```powershell
.\.venv\Scripts\pytest -q
```
