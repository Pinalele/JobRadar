from pathlib import Path
import csv
import string

DATA_FILE = Path(__file__).parent.parent/"data"/"postings.csv"

titles = []
with open(DATA_FILE, encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        if i == 20:
            break
        titles.append(string.capwords(row["title"]))

engineer_roles = [title for title in titles if "Engineer" in title]
senior_roles = [title for title in titles if "Senior" in title]

print(f'Engineer roles: {engineer_roles}')
print(f'Senior roles: {senior_roles}')

lowercase_titles = [title.lower() for title in titles]
print(f'First 3 in lowercase: {lowercase_titles[0:3]}')

short_title = [title for title in titles if len(title.split()) <= 2]
print(f'Short titles (2 words or fewer): {len(short_title)}')
