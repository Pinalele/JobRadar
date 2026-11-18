import string

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

def to_annual_salary(amount: str, pay_period: str) -> float | None:
    """Convert a pay amount to a yearly salary, or return None if the period is unknown."""
    if not amount:
        return None
    try:
        salary = float(amount)
    except ValueError:
        return None
    if pay_period == "YEARLY":
        return salary
    elif pay_period == "MONTHLY":
        return salary * 14
    elif pay_period == "HOURLY":
        return salary * 2080
    else:
        return None


if __name__ == "__main__":
    print(to_annual_salary("50.0", "HOURLY"))
    print(to_annual_salary("abc", "YEARLY"))
    print(to_annual_salary("$3,000", "MONTHLY"))
    print(to_annual_salary("", "YEARLY"))