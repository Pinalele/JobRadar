from pathlib import Path
import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
import sys
sys.path.append(str(Path(__file__).parent.parent))
from matching import is_ai_role

DATA_FILE = Path(__file__).parent.parent/"data"/"postings.csv"

postings_df = pd.read_csv(DATA_FILE)

hourly = postings_df[postings_df["pay_period"] == "HOURLY"]
print(len(hourly))

postings_df_with_salary = postings_df[postings_df["pay_period"].isin(["YEARLY", "MONTHLY", "HOURLY"]) &
                                      postings_df["max_salary"].notna()]

print(len(postings_df_with_salary))

postings_df_is_ai_role = postings_df[postings_df["title"].apply(is_ai_role)]

print(len(postings_df_is_ai_role))
print(postings_df_is_ai_role["title"].head(5))
