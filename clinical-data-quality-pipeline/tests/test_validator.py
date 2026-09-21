import pandas as pd
from quality_pipeline.validator import validate_dataframe
from quality_pipeline.reporting import summarize

def test_complete_without_date_is_error():
    df = pd.DataFrame([{
        "site_id":"AT001","subject_id":"P001","visit_date":pd.NaT,"status":"COMPLETE"
    }])
    issues = validate_dataframe(df)
    assert "COMPLETE_WITHOUT_VISIT_DATE" in set(issues["rule_code"])

def test_invalid_status_is_error():
    df = pd.DataFrame([{
        "site_id":"AT001","subject_id":"P001",
        "visit_date":pd.Timestamp("2026-09-01"),"status":"INVALID"
    }])
    issues = validate_dataframe(df)
    assert "INVALID_STATUS" in set(issues["rule_code"])

def test_summary_counts_error_rows():
    df = pd.DataFrame([
        {"site_id":"AT001","subject_id":"P001","visit_date":pd.NaT,"status":"COMPLETE"},
        {"site_id":"AT001","subject_id":"P002","visit_date":pd.Timestamp("2026-09-01"),"status":"PENDING"},
    ])
    summary = summarize(df, validate_dataframe(df))
    assert summary["total_records"] == 2
    assert summary["rows_with_errors"] == 1
