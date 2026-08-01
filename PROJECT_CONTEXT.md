# PosScraper Project Context

This document is the reusable context file for continuing development in a future session. Update it whenever the architecture, scope, assumptions, or development state changes.

## 1. Project objective

Build a personal career opportunity intelligence system that:

1. collects publicly available job, PhD, and research vacancies;
2. normalises information from different websites;
3. classifies each opportunity into multiple overlapping categories;
4. checks practical eligibility separately from technical suitability;
5. compares each opportunity with a structured candidate evidence base;
6. ranks and explains the most relevant opportunities;
7. learns from decisions such as apply, save, reject, or not eligible.

The system should support comprehensive mechanical-engineering and engineering-AI career exploration rather than only CFD vacancies.

## 2. Candidate context

The intended user has a multidisciplinary mechanical-engineering profile with evidence spanning:

- MSc in Computational Fluid Dynamics;
- BEng in Mechanical Engineering;
- CFD, aerodynamics, thermal-fluid analysis, turbulence modelling, meshing, post-processing, verification, validation, and HPC workflows;
- OpenFOAM, ANSYS Fluent, and STAR-CCM+;
- FEA, structural analysis, fatigue, modal analysis, vibration, NVH, and drivetrain simulation;
- ANSYS Mechanical, NASTRAN, ROMAX, ACTRAN, and some Abaqus exposure;
- mechanical design, vehicle packaging, Siemens NX, CATIA, and SolidWorks;
- Python, MATLAB, Linux, Git, Streamlit, and FastAPI;
- developing AI/ML capability including TensorFlow, Keras, PINNs, CNN concepts, graph-learning concepts, GenAI, and RAG;
- automotive and engineering research experience.

The system must distinguish evidence levels such as professional use, academic use, project use, basic familiarity, and learning interest. It must not exaggerate proficiency.

## 3. Opportunity coverage

### Industry and engineering families

- Mechanical design and product development
- CFD, aerodynamics, fluid mechanics, thermal engineering, and heat transfer
- FEA, structural mechanics, structural dynamics, NVH, fatigue, and durability
- General CAE, multiphysics, simulation validation, and engineering automation
- Automotive, aerospace, energy, hydrogen, batteries, turbomachinery, and manufacturing
- Robotics, soft robotics, mechatronics, controls, autonomous systems, and digital twins
- Applied AI/ML, scientific ML, surrogate modelling, reduced-order modelling, PINNs, graph ML, and optimisation
- GenAI, RAG, engineering knowledge systems, and engineering software development
- Application engineering, technical consulting, research engineering, and numerical/HPC roles

### PhD and research families

- CFD, turbulence, aerodynamics, wind engineering, multiphase flow, sloshing, combustion, reacting flows, and heat transfer
- Computational mechanics, structures, composites, fatigue, fracture, biomechanics, and fluid-structure interaction
- Robotics, soft robotics, microrobotics, medical robotics, controls, smart materials, and actuation
- Scientific machine learning, PINNs, neural operators, graph neural networks, uncertainty quantification, inverse problems, and simulation acceleration
- Automotive, aerospace, energy, hydrogen, batteries, thermal packaging, materials, manufacturing, and sustainability

An opportunity can have one primary family and several secondary families, domains, methods, tools, and research topics.

## 4. Required scoring dimensions

Do not rely on one unexplained match percentage. Keep at least these dimensions separate:

- Technical fit
- Transferable fit
- Eligibility fit
- Preference fit
- Competitiveness
- Evidence strength
- Application urgency

Industry and PhD positions require different scoring logic. PhD assessment should value research foundations and transferable methods rather than demand prior work on the exact research application.

## 5. Planned architecture

```text
Sources and public APIs
        ↓
Source-specific collectors
        ↓
Normalised opportunity model
        ↓
Deduplication and freshness checks
        ↓
Multi-label classification
        ↓
Hard eligibility filters
        ↓
Candidate-evidence retrieval
        ↓
Role-specific or PhD-specific scoring
        ↓
Optional LLM assessment
        ↓
Dashboard and feedback loop
```

### Likely technology stack

- Python
- Pydantic for schemas and validation
- httpx for API requests
- Beautiful Soup and/or Scrapy for permitted static-page collection
- Playwright only for necessary JavaScript-rendered pages
- SQLite initially, PostgreSQL later if required
- Sentence Transformers or hosted embeddings for semantic retrieval
- Optional LLM with structured output for complex extraction and explanation
- Streamlit for the first dashboard
- FastAPI only when a separate backend becomes useful
- pytest for automated tests

## 6. Development principles

- Work in small, understandable steps.
- Explain each completed step before starting the next one.
- Keep documentation and this context file current.
- Add tests alongside meaningful behaviour.
- Prefer APIs and stable structured endpoints over browser scraping.
- Respect website terms, robots directives, rate limits, and access controls.
- Do not bypass CAPTCHAs, logins, or anti-bot protections.
- Do not automatically submit applications in early versions.
- Keep deterministic rules separate from probabilistic AI judgements.
- Store the evidence behind each recommendation so results remain explainable.
- Never treat missing visa, funding, salary, or eligibility information as confirmed.

## 7. Local development environment

Repository:

```text
https://github.com/WAniruddha/PosScraper.git
```

Windows virtual environment:

```text
D:\02_Applications\10_VEnv\E1
```

Expected activation command:

```powershell
& "D:\02_Applications\10_VEnv\E1\Scripts\Activate.ps1"
```

Install the local project in editable mode:

```powershell
python -m pip install -e ".[dev]"
```

## 8. Current development state

### Completed: Step 1

- Repository initialised with documentation.
- Standard `src` package structure introduced.
- Minimal CLI environment check introduced.
- Initial smoke test introduced.
- Local setup documented for the selected virtual environment.

### Next: Step 2

Define and test the normalised opportunity schema, including:

- industry, PhD, research, internship, contract, and graduate opportunity types;
- primary and secondary categories;
- domains, methods, software, required and preferred skills;
- seniority and experience ranges;
- education requirements;
- location, work arrangement, sponsorship, and eligibility;
- PhD funding and international-funding eligibility;
- posted date, deadline, source URL, application URL, and source metadata.

No scraping should begin until the data model is clear enough to receive information consistently from multiple sources.
