import os
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://clinical:clinical@localhost:5432/clinical_quality"
)

def get_engine():
    return create_engine(DATABASE_URL, future=True)

def init_db():
    with get_engine().begin() as conn:
        conn.execute(text(
            "CREATE TABLE IF NOT EXISTS validation_issues ("
            "id BIGSERIAL PRIMARY KEY,"
            "row_index INTEGER NOT NULL,"
            "severity VARCHAR(20) NOT NULL,"
            "rule_code VARCHAR(100) NOT NULL,"
            "message TEXT NOT NULL,"
            "created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP)"
        ))

def save_issues(issues):
    if not issues.empty:
        issues.to_sql("validation_issues", get_engine(), if_exists="append", index=False)
