from pathlib import Path
import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

DATA_FILE = Path(__file__).parent.parent/"data"/"postings.csv"

postings_df = pd.read_csv(DATA_FILE)
print(postings_df.shape)

print(list(postings_df.columns))

print(postings_df[["title", "company_name", "max_salary", "pay_period"]].head())

print(postings_df["max_salary"].dtype)
print(postings_df["title"].dtype)

print(postings_df["max_salary"].head(10))