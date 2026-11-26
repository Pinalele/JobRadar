import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))

from matching import is_ai_role
from cleaning import get_city
DATA_FILE = Path(__file__).parent.parent/"data"/"postings.csv"

postings_df = pd.read_csv(DATA_FILE)

postings_df_is_ai_role = postings_df[postings_df["title"].apply(is_ai_role)].copy()

print(postings_df["pay_period"].value_counts())
print(postings_df["pay_period"].value_counts(dropna=False))


print(postings_df["company_name"].value_counts())
print(postings_df["company_name"].value_counts(dropna=False))


postings_df_company = postings_df_is_ai_role["company_name"].value_counts().head(10)

print(postings_df_company)

print(postings_df.groupby("pay_period")["max_salary"].median())


postings_df_is_ai_role["city"] = postings_df_is_ai_role["location"].apply(get_city)
print(postings_df_is_ai_role["city"].value_counts().head(10))