from pathlib import Path
import csv
import string

DATA_FILE = Path(__file__).parent.parent/"data"/"sample_postings.csv"

titles = []
with open(DATA_FILE, encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = string.capwords(row["title"])
        titles.append(title)

print(f'Number of titles: {len(titles)}')
print(f'First: {titles[0]}')
print(f'Last: {titles[-1]}')
is_data_scientist_present = "Data Scientist" in titles
print(f'Has "Data Scientist": {is_data_scientist_present}')
is_product_manager_present = "Product Manager" in titles
print(f'Has "Product Manager": {is_product_manager_present}')