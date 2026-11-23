import pytest

from matching import is_ai_role, skills_in, words_in_text


@pytest.mark.parametrize("title, expected", [
    ("Machine Learning Engineer", True),
    ("Senior AI Researcher", True),
    ("AI/ML Engineer", True),
    ("LLM Platform Engineer", True),
    ("Senior Engineer (AI)", True),
    ("Retail Salesperson", False),
    ("Email Copywriter", False),
    ("Accountant", False),
])
def test_is_ai_role(title, expected):
    assert is_ai_role(title) == expected


@pytest.mark.parametrize("description, expected", [
    ("We need Python, SQL and AWS.", {"python", "sql", "aws"}),
    ("Deep learning experience is a plus.", {"deep learning"}),
    ("No technical skills required.", set()),
    ("Skills: Python; SQL.", {"python", "sql"}),
])
def test_skills_in(description, expected):
    assert skills_in(description) == expected


def test_words_in_text():
    assert words_in_text("Skills: Python; SQL (AWS).") == ["skills", "python", "sql", "aws"]