import argparse, json
from pathlib import Path
import pandas as pd

from .validator import validate_dataframe
from .reporting import summarize
from .db import init_db, save_issues

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--save-db", action="store_true")
    parser.add_argument("--issues-out", type=Path, default=Path("validation_issues.csv"))
    args = parser.parse_args()

    df = pd.read_csv(args.csv_file, parse_dates=["visit_date"])
    issues = validate_dataframe(df)
    summary = summarize(df, issues)
    issues.to_csv(args.issues_out, index=False)

    if args.save_db:
        init_db()
        save_issues(issues)

    print(json.dumps(summary, indent=2))
    print(f"Issues written to {args.issues_out}")

if __name__ == "__main__":
    main()
