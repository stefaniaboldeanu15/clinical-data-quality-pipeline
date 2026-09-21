def summarize(records, issues):
    error_rows = set(issues.loc[issues["severity"] == "ERROR","row_index"]) if not issues.empty else set()
    warning_rows = set(issues.loc[issues["severity"] == "WARNING","row_index"]) if not issues.empty else set()
    total = len(records)
    return {
        "total_records": int(total),
        "valid_records": int(total - len(error_rows)),
        "rows_with_errors": int(len(error_rows)),
        "rows_with_warnings": int(len(warning_rows)),
        "error_rate_pct": round(len(error_rows) / total * 100, 2) if total else 0.0
    }
