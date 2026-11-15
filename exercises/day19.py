posting_a = {"title": "ML Engineer", "skills": ["python", "pytorch", "sql", "aws", "python"]}
posting_b = {"title": "Data Scientist", "skills": ["python", "sql", "pandas", "statistics"]}
my_skills = {"python", "sql", "pandas"}

skills_a = set(posting_a.get("skills"))
skills_b = set(posting_b.get("skills"))
all_skills = skills_a | skills_b
common = skills_a & skills_b
missing = skills_a - my_skills

print(f'{posting_a.get('title')} skills: {len(posting_a.get("skills"))} in the list, {len(skills_a)} unique ')

print(f'Common skills: {sorted(common)}')
print(f'All skills: {sorted(all_skills)}')
print(f'Missing for ML Engineer: {sorted(missing)}')