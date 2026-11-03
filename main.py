title = "   senior Machine Learning ENGINEER  "
company = "Acme AI Labs"
location = "Lisbon, Portugal"
max_salary = "65000.0"
pay_period = "YEARLY"

title = title.strip().title()

is_ml_role = 'machine learning' in title.lower()

location = location.split(",")
city = location[0]

max_salary = float(max_salary)
salary_twelve = max_salary / 12
salary_fourteen = max_salary / 14


print(f'{title} @ {company} ({city})')
print(f'ML role: {is_ml_role}')
print(f'Annual salary: {max_salary:,.2f}')
print(f'Monthly (12x): {salary_twelve:,.2f}')
print(f'Monthly (14x): {salary_fourteen:,.2f}')