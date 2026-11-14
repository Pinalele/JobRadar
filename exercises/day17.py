from collections import Counter, defaultdict

postings = [
    {"title": "ML Engineer", "company": "Acme AI Labs", "city": "Lisbon"},
    {"title": "Data Scientist", "company": "DataCo", "city": "Porto"},
    {"title": "AI Engineer", "company": "Acme AI Labs", "city": "Porto"},
    {"title": "LLM Engineer", "company": "Robo Inc", "city": "Lisbon"},
    {"title": "MLOps Engineer", "company": "Acme AI Labs", "city": "Lisbon"},
    {"title": "Data Analyst", "company": "DataCo", "city": "Braga"},
]

offers = [posting.get("company") for posting in postings]
counter = Counter(offers)

print("Postings per company:")
for company, count in counter.most_common():
    print(f'{company}: {count}')


cities = [posting.get("city") for posting in postings]
city_count = Counter(cities)
for city, count in city_count.most_common(1):
    print(f'Most common city: {city} ({count})')

# Groups role per city
titles_by_city = defaultdict(list)
for posting in postings:
    titles_by_city[posting["city"]].append(posting.get('title'))

for city, titles in titles_by_city.items():
    print(f'{city}: {titles}')