postings = [
    {"title": "Machine Learning Engineer", "company": "Acme AI Labs", "city": "Lisbon", "annual_salary": 104000.0, "remote": True},
    {"title": "Data Scientist", "company": "DataCo", "city": "Porto", "annual_salary": 42000.0},
    {"title": "AI Engineer", "company": "Robo Inc", "city": "Braga", "remote": False},
]
remote_count = 0
for row in postings:
    if row.get("remote", False):
        remote_count += 1
    salary = row.get("annual_salary")
    if salary is None:
        print(f"{row.get("title")} @ {row.get("company")} ({row.get("city")}): salary not available")
    else:
        print(f"{row.get("title")} @ {row.get("company")} ({row.get("city")}): {salary:,.2f}")

print(f"Remote postings: {remote_count}")