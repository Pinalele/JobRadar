posting = {
    "title": "Machine Learning Engineer",
    "company": "Acme AI Labs",
    "city": "Lisbon",
    "annual_salary": 104000.0,
}

print(f"Title: {posting["title"]}")
print(f"Company: {posting["company"]}")
print(f"Remote: {posting.get("remote", "not specified")}")
posting["remote"] = True
print(f"Remote: {posting.get("remote", "not specified")}")
posting["annual_salary"] = 110000.0
print(f"New salary: {posting.get("annual_salary"):,.2f}")
del posting["city"]
print(f"Has city: {"city" in posting}")
print(f"Number of fields: {len(posting)}")
print(f"Fields: {list(posting.keys())}")

