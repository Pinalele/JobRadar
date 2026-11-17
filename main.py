import csv
from collections import Counter
from cleaning import clean_title, get_city, clean_company, to_annual_salary
from matching import is_ai_role, skills_in


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

most_recent = sorted(ai_postings, key=listed_time_of, reverse=True)

for row in most_recent[0:20]:
    print(row["title"])


print(f"AI postings: {len(ai_postings)}")
ai_posting_companies = [clean_company(posting["company_name"]) for posting in ai_postings if clean_company(posting["company_name"]) != "Unknown company"]
company_counter = Counter(ai_posting_companies)
print("Top 10 companies hiring for AI:")
for i, (company, count) in enumerate(company_counter.most_common(10), start=1):
    print(f"{i}. {company}: {count}")



ai_posting_cities = [get_city(posting["location"]) for posting in ai_postings if get_city(posting["location"]) != "Remote / unspecified"]
city_counter = Counter(ai_posting_cities)
print("Top 10 cities for AI jobs:")
for i, (city, count) in enumerate(city_counter.most_common(10), start=1):
    print(f"{i}. {city}: {count}")

ai_salaries = [to_annual_salary(posting["max_salary"], posting["pay_period"]) for posting in ai_postings if to_annual_salary(posting["max_salary"], posting["pay_period"]) is not None]
print(f'AI postings with salary: {len(ai_salaries)} of {len(ai_postings)} ({(len(ai_salaries) / len(ai_postings)):.1%})')
print(f'Average AI salary: {sum(ai_salaries) / len(ai_salaries):,.2f}')


all_skills = []

for posting in ai_postings:
    all_skills.extend(skills_in(posting["description"]))

counter = Counter(all_skills)

print("Top 15 skills in AI postings:")
for i, (skill, count) in enumerate(counter.most_common(15), start=1):
    print(f"{i}. {skill}: {count} ({count / len(ai_postings):.1%})")