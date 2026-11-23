import pytest
from matching import is_ai_role, skills_in


@pytest.mark.parametrize("title, expected", [("Machine Learning Engineer", True),
                                             ("Senior AI Researcher", True),
                                             ("AI/ML Engineer", True),
                                             ("LLM Platform Engineer", True),
                                             ("Retail Salesperson", False),
                                             ("Email Copywriter", False),
                                             ("Accountant", False)])
def test_is_ai_role(title, expected):
    assert is_ai_role(title) == expected


@pytest.mark.parametrize("description, expected", [("We need Python, SQL and AWS.", {"python", "sql", "aws"}),
                                                     ("Deep learning experience is a plus.", {"deep learning"}),
                                                     ("No technical skills required.", set()),
                                                     ("Skills: Python; SQL.", {"python", "sql"}),
                                                     ])
def test_skills_in(description, expected):
    assert skills_in(description) == expected
