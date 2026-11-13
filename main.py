import csv
import string

ai_words = ["ai", "ml", "llm"]
ai_phrases = ["artificial intelligence", "machine learning"]


def clean_title(title: str) -> str:
    """Return the title without extra spaces and with each word capitalised."""
    return string.capwords(title)


def get_city(location: str) -> str:
    """Return the city from a location like 'Lisbon, Portugal'."""
    if location == "United States":
        return "Remote / unspecified"
    else:
        return location.split(",")[0].strip()


def clean_company(name: str) -> str:
    """Return the company name without extra spaces, or 'Unknown company' if empty."""
    name = name.strip()
    if not name:
        return "Unknown company"
    return name

def is_ai_role(title: str) -> bool:
    """Return True if the title mentions AI or machine learning."""
    for keyword in ai_phrases:
        if keyword in title.lower():
            return True
    for keyword in ai_words:
        if keyword in title.lower().replace("/", " ").split():
            return True
    return False

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


def project_salary(annual_salary: float, target: float, years: int = 5, raise_rate: float = 0.03) -> None:
    """Print the yearly salary with annual raises until the target is reached."""
    for year in range(1, years + 1):
        print(f"Year {year}: {annual_salary:,.2f}")
        if annual_salary >= target:
            print(f"Target of {target:,.2f} reached in year {year}")
            break
        annual_salary *= 1 + raise_rate
    else:
        print(f"Target not reached in {years} years")

def listed_time_of(row):
    """Return when the posting was listed, as a number."""
    return float(row["listed_time"])
ai_postings = []

total = 0
with_salary = 0
yearly = 0
monthly = 0
hourly = 0
empty_period = 0
other_period = 0



with open("data/postings.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        if is_ai_role(row["title"]):
            ai_postings.append(row)
        total += 1
        annual_salary = to_annual_salary(row["max_salary"], row["pay_period"])
        pay_period = row["pay_period"]
        if pay_period == "YEARLY":
            yearly += 1
        elif pay_period == "MONTHLY":
            monthly += 1
        elif pay_period == "HOURLY":
            hourly += 1
        elif pay_period == "":
            empty_period += 1
        else:
            other_period += 1
        title = clean_title(row["title"])
        city = get_city(row["location"])
        company = clean_company(row["company_name"])
        if annual_salary is None:
            salary_text = "salary not available"
        else:
            salary_text = f"{annual_salary:,.2f}"
            with_salary += 1
        if i < 20:
            print(f'{i + 1} - {title} @ {company} ({city}): {salary_text}')

print(f"Total postings: {total}")
print(f"With salary: {with_salary} ({with_salary / total:.1%})")
print(f"YEARLY: {yearly}")
print(f"MONTHLY: {monthly}")
print(f"HOURLY: {hourly}")
print(f"Empty: {empty_period}")
print(f"Other: {other_period}")

most_recent = sorted(ai_postings, key=listed_time_of, reverse= True)

for row in most_recent[0:20]:
    print(row["title"])


print(f"AI postings: {len(ai_postings)}")

