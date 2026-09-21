import pandas as pd

ALLOWED_STATUSES = {"COMPLETE", "PENDING", "MISSING", "QUERY_OPEN"}

def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    required = {"site_id", "subject_id", "visit_date", "status"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    issues = []
    duplicates = df.duplicated(subset=["site_id","subject_id","visit_date"], keep=False)

    for idx, row in df.iterrows():
        if pd.isna(row["site_id"]) or str(row["site_id"]).strip() == "":
            issues.append(_issue(idx,"ERROR","MISSING_SITE_ID","site_id is required"))

        if pd.isna(row["subject_id"]) or str(row["subject_id"]).strip() == "":
            issues.append(_issue(idx,"ERROR","MISSING_SUBJECT_ID","subject_id is required"))

        if row["status"] not in ALLOWED_STATUSES:
            issues.append(_issue(idx,"ERROR","INVALID_STATUS",
                f"status must be one of {sorted(ALLOWED_STATUSES)}"))

        if row["status"] == "COMPLETE" and pd.isna(row["visit_date"]):
            issues.append(_issue(idx,"ERROR","COMPLETE_WITHOUT_VISIT_DATE",
                "COMPLETE records require visit_date"))

        if duplicates.loc[idx]:
            issues.append(_issue(idx,"WARNING","POSSIBLE_DUPLICATE",
                "Duplicate site/subject/visit_date combination"))

    return pd.DataFrame(issues, columns=["row_index","severity","rule_code","message"])

def _issue(row_index, severity, rule_code, message):
    return {
        "row_index": int(row_index),
        "severity": severity,
        "rule_code": rule_code,
        "message": message
    }
