from pathlib import Path
import csv
import string

DATA_FILE = Path(__file__).parent.parent/"data"/"postings.csv"

titles = []
with open(DATA_FILE, encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        if i == 12:
            break
        titles.append(string.capwords(row["title"]))

page_size = 5
for start in range(0, len(titles), page_size):
    page = titles[start:start + page_size]
    page_number = start // page_size + 1
    print(f'\nPage {page_number}:')
    for title in page:
        print(f'  {title}')

shortlist = []

shortlist.append('Building Engineer')
shortlist.append('Project Architect')
shortlist.append('Producer')
shortlist.insert(0, "Service Technician")
shortlist.remove('Producer')
removed = shortlist.pop(-1)

print(f'Removed: {removed}')
print(f'Shortlist: {shortlist}')
postion = shortlist.index("Building Engineer")
print(f"Position of 'Building Engineer': {postion}")