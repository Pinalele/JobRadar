postings = [
    {"title": "ML Engineer", "company": "Acme AI Labs", "city": "Lisbon", "annual_salary": 104000.0},
    {"title": "Data Scientist", "company": "DataCo", "city": "Porto", "annual_salary": 42000.0},
    {"title": "AI Engineer", "company": "Acme AI Labs", "city": "Porto", "annual_salary": 95000.0},
    {"title": "LLM Engineer", "company": "Robo Inc", "city": "Lisbon", "annual_salary": 120000.0},
    {"title": "MLOps Engineer", "company": "Acme AI Labs", "city": "Lisbon", "annual_salary": 88000.0},
    {"title": "Data Analyst", "company": "DataCo", "city": "Braga", "annual_salary": 38000.0},
]

salary_by_title = {posting.get("title"): posting.get("annual_salary") for posting in postings}
high_salaries = {posting.get("title"): posting.get("annual_salary") for posting in postings if posting.get("annual_salary") >= 90000 }

print(f'LLM Engineer salary: {salary_by_title.get("LLM Engineer"):,.2f}')
print(f'High salaries: {high_salaries}')

summary = {}

for posting in postings:
    city = posting.get("city")
    if city not in summary:
        summary[city] = {"count": 0, "total_salary": 0.0}
    summary[city]["count"] += 1
    summary[city]["total_salary"] += posting["annual_salary"]

for city, data in summary.items():
    average = data["total_salary"] / data["count"]
    print(f'{city}: {data["count"]} postings, average salary {average:,.2f}')