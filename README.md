# Exploratory Data Analysis Toolkit

<!-- project-guide:start -->
## Project guide

[Project architecture](PROJECT_ARCHITECTURE.md) · [Interview questions and answers](INTERVIEW_QA.md)

Use the architecture document for the component diagram, implementation boundaries, and verification entry points. The interview guide includes source-backed answers and project walkthroughs.

### Implementation map

| Component | Responsibility |
| --- | --- |
| [`src/eda/main.py`](src/eda/main.py) | HTTP handlers: `GET /healthz`, `POST /analyze` |
| [`src/eda/ops.py`](src/eda/ops.py) | HTTP handlers: `GET /readyz`, `POST /workspaces`, `GET /workspaces`, `POST /workspaces/{workspace_id}/jobs`, `GET /jobs/{job_id}` |
| [`src/eda/analyze.py`](src/eda/analyze.py) | Functions: `analyze` |
| [`requirements.txt`](requirements.txt) | Implementation or supporting configuration |
| [`src/eda/__init__.py`](src/eda/__init__.py) | Implementation or supporting configuration |
| [`Dockerfile`](Dockerfile) | Container build/service configuration |
| [`Makefile`](Makefile) | Implementation or supporting configuration |
| [`docker-compose.yml`](docker-compose.yml) | Container build/service configuration |
| [`tests/test_analyze.py`](tests/test_analyze.py) | Executable checks and regression examples |
| [`tests/test_ops.py`](tests/test_ops.py) | Executable checks and regression examples |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | GitHub Actions job definitions |
| [`README.md`](README.md) | Project explanations or operating notes |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Project explanations or operating notes |

### Local setup and verification

From the repository root (the commands follow the checked-in manifests):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

To serve the FastAPI application locally, install the server separately if it is not already available:

```bash
python -m pip install uvicorn
PYTHONPATH=src python -m uvicorn eda.main:app --reload
```

<!-- project-guide:end -->

Level: 1 — Python, Data & Automation

Skills: Python, summaries, grouping

Profile numeric `value` grouped by `cohort`. Returns mean, median, min, max, and skipped non-numeric cells.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.

## Ops plane

Workspaces, tenant isolation, job approval, and audit live under `/v1`. Production apply is refused. See `docs/ARCHITECTURE.md`.
