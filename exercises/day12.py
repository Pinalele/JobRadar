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

pairs = [(string.capwords(row["title"]), to_annual_salary(row["max_salary"], row["pay_period"])) for row in lines if to_annual_salary(row["max_salary"], row["pay_period"]) is not None]
print(f"First pair: {pairs[0]}")

title, salary = pairs[0]

print(f"Title: {title} | Salary: {salary:,.2f}")

for i, row in enumerate(pairs, start=1):
    title, salary = row
    print(f"{i}. Title: {title} | Salary: {salary:,.2f}")

titles = [pair[0] for pair in pairs]
salaries = [pair[1] for pair in pairs]


print("Over 100,000:")
for title, salary in zip(titles, salaries):
    if salary > 100000:
        print(f"{title}: {salary:,.2f}")
