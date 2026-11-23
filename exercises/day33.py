postings = [
    {"title": "ML Engineer", "salary": "104000"},
    {"title": "Data Scientist", "salary": "42000"},
    {"title": "AI Engineer", "salary": ""},
    {"title": "LLM Engineer", "salary": "120000"},
]


def parse_salary(text):
    if text == "":
        return 0
    return int(text)


def average_salary(postings):
    total = 0
    count = 0
    for posting in postings:
        salary = parse_salary(posting["salary"])
        total += salary
        if salary == 0:
            continue
        count += 1
    return total / count


def best_paid(postings):
    best = postings[0]
    for posting in postings[1:]:
        if parse_salary(posting["salary"]) > parse_salary(best["salary"]):
            best = posting
    return best


def titles_upper(postings):
    result = []
    for i in range(len(postings)):
        result.append(postings[i]["title"].upper())
    return result


print(f"Average salary: {average_salary(postings):,.2f}")
print(f"Best paid: {best_paid(postings)['title']}")
print(f"Titles: {titles_upper(postings)}")