from pathlib import Path
import csv
import string

DATA_FILE = Path(__file__).parent.parent/"data"/"postings.csv"

def to_annual_salary(amount: str, pay_period: str) -> float | None:
    """Convert a pay amount to a yearly salary, or return None if the period is unknown."""
    if not amount:
        return None
    salary = float(amount)
    if pay_period == "YEARLY":
        return salary
    elif pay_period == "MONTHLY":
        return salary * 14
    elif pay_period == "HOURLY":
        return salary * 2080
    else:
        return None



lines = []
with open(DATA_FILE, encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        if i == 20:
            break
        lines.append(row)

# just give us the one that have salary
filter_lines = [ row for row in lines if to_annual_salary(row["max_salary"], row["pay_period"]) is not None]

def annual_salary_of(row):
    return to_annual_salary(row["max_salary"], row["pay_period"])

# uses annual_salary_of to get the value of salary and puts in a DESC order
highest_first = sorted(filter_lines, key=annual_salary_of, reverse=True)

print("Highest paid:")
# prints the first thress high salary's
for i, row in enumerate(highest_first[0:3]):
    print(f'{i+1}. {string.capwords(row["title"])}: {annual_salary_of(row):,.2f}')

lowest_first = sorted(filter_lines, key=annual_salary_of)
print("Lowest paid:")
# prints the first thress high salary's
for i, row in enumerate(lowest_first[0:3]):
    print(f'{i+1}. {string.capwords(row["title"])}: {annual_salary_of(row):,.2f}')

titles = [string.capwords(row["title"]) for row in filter_lines]
titles.sort()
print(f'First 3 alphabetically:')
print(titles[0:3])



