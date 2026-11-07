# JobRadar - Days 2 and 3: process one job posting

# Raw posting (as it would come from the CSV)
title = "   senior Machine Learning ENGINEER  "
company = "Acme AI Labs"
location = "Lisbon, Portugal"
max_salary = "50.0"
pay_period = "HOURLY"

# Day 2: clean the text fields
clean_title = title.strip().title()
is_ml_role = "machine learning" in clean_title.lower()
city = location.split(",")[0]

print(f"{clean_title} @ {company} ({city})")
print(f"ML role: {is_ml_role}")

# Day 3, Part A: convert the pay to a yearly salary
salary = float(max_salary)

if pay_period == "YEARLY":
    annual_salary = salary
elif pay_period == "MONTHLY":
    annual_salary = salary * 14
elif pay_period == "HOURLY":
    annual_salary = salary * 2080
else:
    print(f"Unknown pay period: {pay_period}")
    annual_salary = None

if annual_salary is not None:
    # Day 2: yearly and monthly amounts
    print(f"Annual salary: {annual_salary:,.2f}")
    print(f"Monthly (12x): {annual_salary / 12:,.2f}")
    print(f"Monthly (14x): {annual_salary / 14:,.2f}")

    # Day 3, Part B: 5-year projection
    target = 110000

    for year in range(1, 6):
        print(f"Year {year}: {annual_salary:,.2f}")
        if annual_salary >= target:
            print(f"Target of {target:,.2f} reached in year {year}")
            break
        annual_salary *= 1.03
    else:
        print("Target not reached in 5 years")