import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))

from matching import is_ai_role
DATA_FILE = Path(__file__).parent.parent/"data"/"postings.csv"

postings_df = pd.read_csv(DATA_FILE)

postings_df_is_ai_role = postings_df[postings_df["title"].apply(is_ai_role)].copy()

print(postings_df_is_ai_role[["title", "company_name", "location", "max_salary", "pay_period"]].isna().sum())


percentage_with_salary = postings_df_is_ai_role["max_salary"].notna().mean()

print(f"percentage with salary is: {percentage_with_salary:.1%}")

postings_df_is_ai_role["listed_date"] = pd.to_datetime(postings_df_is_ai_role["listed_time"], unit="ms")

print(postings_df_is_ai_role["listed_date"].min())
print(postings_df_is_ai_role["listed_date"].max())

sorted_date = postings_df_is_ai_role.sort_values("listed_date", ascending=False)
print(sorted_date[["title", "listed_date"]].head())

print(postings_df_is_ai_role["company_name"].fillna("Unknown company").value_counts().head(10))