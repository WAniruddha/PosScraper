# PosScraper

PosScraper is a personal **career opportunity intelligence system** for discovering, classifying, evaluating, and prioritising relevant industry jobs, PhD positions, and research opportunities.

The project is being built incrementally. Each step should remain understandable, testable, and documented before the next layer is added.

## Intended opportunity coverage

PosScraper is designed to support overlapping career tracks rather than a single job category:

- Mechanical design and product development
- CFD, aerodynamics, fluid mechanics, and thermal engineering
- FEA, structural mechanics, NVH, fatigue, and general CAE
- Automotive, aerospace, energy, and engineering R&D
- Robotics, mechatronics, controls, and soft robotics
- Applied AI/ML, scientific machine learning, PINNs, and surrogate modelling
- GenAI, RAG, engineering automation, and engineering software
- Mechanical-engineering-related PhD and research positions

A vacancy may belong to several categories simultaneously.

## Development approach

The system will eventually contain five main layers:

1. **Collection**: retrieve vacancies from public APIs and permitted career pages.
2. **Normalisation**: convert different source formats into one consistent opportunity schema.
3. **Classification**: assign multiple role, research, domain, skill, and seniority labels.
4. **Matching**: compare each vacancy with a structured candidate evidence base using rules, embeddings, and optional LLM evaluation.
5. **Decision support**: explain fit, gaps, eligibility, urgency, and the recommended application strategy.

The first versions will retain a human approval step. PosScraper will not automatically submit applications.

## Step 1: project foundation

The current version establishes:

- a standard Python `src` project layout;
- a small command-line environment check;
- package metadata in `pyproject.toml`;
- a smoke test;
- Windows setup instructions for the selected virtual environment;
- reusable project context in `PROJECT_CONTEXT.md`.

No website scraping, AI model, or database is introduced in Step 1. This keeps the foundation small enough to verify before adding moving parts.

## Local setup on Windows

The selected virtual environment is:

```text
D:\02_Applications\10_VEnv\E1
```

Open PowerShell and run:

```powershell
cd <PATH-WHERE-YOU-WANT-THE-PROJECT>
git clone https://github.com/WAniruddha/PosScraper.git
cd PosScraper

& "D:\02_Applications\10_VEnv\E1\Scripts\Activate.ps1"
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell blocks activation for the current session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
& "D:\02_Applications\10_VEnv\E1\Scripts\Activate.ps1"
```

## Verify the installation

Run the environment check:

```powershell
pos-scraper doctor
```

Equivalent module command:

```powershell
python -m pos_scraper.cli doctor
```

Run the tests:

```powershell
pytest
```

The environment check should report the PosScraper version, Python version, executable path, platform, and current working directory.

## Project structure

```text
PosScraper/
├── src/
│   └── pos_scraper/
│       ├── __init__.py
│       └── cli.py
├── tests/
│   └── test_cli.py
├── .gitignore
├── PROJECT_CONTEXT.md
├── README.md
└── pyproject.toml
```

## Planned next step

Step 2 will define the first proper data model for a normalised opportunity. It will separate industry jobs from PhD/research positions while supporting multi-label categories, requirements, dates, locations, eligibility, funding, and source metadata.
