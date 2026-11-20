from pathlib import Path
import json

postings = [
    {"title": "ML Engineer", "company": "Acme AI Labs", "city": "Lisbon", "annual_salary": 104000.0},
    {"title": "Data Scientist", "company": "DataCo", "city": "Porto", "annual_salary": 42000.0},
    {"title": "AI Engineer", "company": "Robo Inc", "city": "Braga", "annual_salary": None},
]

OUTPUT_FILE = Path(__file__).parent.parent / "data" / "day26_postings.json"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(postings, f, indent=4)

with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
    postings_json = json.load(f)

print(f'Saved {len(postings)} postings to {OUTPUT_FILE.name}')

print(f'Loaded {len(postings_json)} postings')

for posting in postings_json:
    print(posting['title'])

print(f"Same data: {postings_json == postings}")
print(f"Exists: {OUTPUT_FILE.exists()} | Name: {OUTPUT_FILE.name} | Suffix: {OUTPUT_FILE.suffix}")

