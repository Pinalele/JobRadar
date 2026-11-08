# JobRadar - Day 5: read job postings from a CSV file.
import csv

def clean_title(title: str) -> str:
    """Return the title without extra spaces and with each word capitalised."""
    return title.strip().title()

def get_city(location: str) -> str:
    """Return the city from a location like 'Lisbon, Portugal'."""
    return location.split(",")[0].strip()

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


with open("data/sample_postings.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        annual_salary = to_annual_salary(row["max_salary"], row["pay_period"])
        title = clean_title(row["title"])
        city = get_city(row["location"])
        if annual_salary is None:
            salary_text = "salary not available"
        else:
            salary_text = f"{annual_salary:,.2f}"
        print(f'{title} @ {row["company_name"]} ({city}): {salary_text}')