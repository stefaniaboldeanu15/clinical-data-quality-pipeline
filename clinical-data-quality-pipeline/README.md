# Clinical Data Quality Pipeline

A data-engineering portfolio project for validating clinical-style operational datasets and producing reproducible quality reports.

## Stack

Python · pandas · PostgreSQL · SQLAlchemy · pytest · Docker · GitHub Actions

## Validation rules

- missing site IDs
- missing subject IDs
- invalid workflow statuses
- COMPLETE records without visit dates
- possible duplicate business keys

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m quality_pipeline.main data/sample_clinical_records.csv
```

## Tests

```bash
pytest -q
```

## Optional PostgreSQL persistence

```bash
docker compose up -d
PYTHONPATH=src python -m quality_pipeline.main data/sample_clinical_records.csv --save-db
```

## Why this project

It demonstrates how domain data-quality requirements can be translated into explicit validation rules, tests, structured outputs, and relational persistence.
