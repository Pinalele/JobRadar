# JobRadar - Day 4: process one job posting with functions


def clean_title(title: str) -> str:
    """Return the title without extra spaces and with each word capitalised."""
    return title.strip().title()


def get_city(location: str) -> str:
    """Return the city from a location like 'Lisbon, Portugal'."""
    return location.split(",")[0].strip()


def to_annual_salary(amount: str, pay_period: str) -> float | None:
    """Convert a pay amount to a yearly salary, or return None if the period is unknown."""
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


# Raw posting (as it would come from the CSV)
title = "   senior Machine Learning ENGINEER  "
company = "Acme AI Labs"
location = "Lisbon, Portugal"
max_salary = "50.0"
pay_period = "HOURLY"

title_clean = clean_title(title)
print(f"{title_clean} @ {company} ({get_city(location)})")
print(f"ML role: {'machine learning' in title_clean.lower()}")

annual_salary = to_annual_salary(max_salary, pay_period)
if annual_salary is None:
    print(f"Unknown pay period: {pay_period}")
else:
    print(f"Annual salary: {annual_salary:,.2f}")
    project_salary(annual_salary, 110000)