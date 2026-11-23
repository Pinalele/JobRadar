import pytest
from cleaning import clean_title, to_annual_salary, get_city, clean_company


@pytest.mark.parametrize("title, expected", [("  data scientist  ", "Data Scientist"),
                                             ("machine learning ENGINEER", "Machine Learning Engineer"),
                                             ("women's business center", "Women's Business Center"),
                                             ("ai engineer", "AI Engineer")])
def test_clean_title(title, expected):
    assert clean_title(title) == expected


@pytest.mark.parametrize("salary_input, pay_period, expected", [("65000.0", "YEARLY", 65000.0),
                                                                ("3000.0", "MONTHLY", 42000.0),
                                                                ("50.0", "HOURLY", 104000.0),
                                                                ("900.0", "WEEKLY", None),
                                                                ("", "YEARLY", None),
                                                                ("$3,000", "MONTHLY", None)])
def test_to_annual_salary(salary_input, pay_period, expected):
    assert to_annual_salary(salary_input, pay_period) == expected



@pytest.mark.parametrize("city, expected", [("Lisbon, Portugal", "Lisbon"),
                                                ("United States", "Remote / unspecified"),
                                                ("Greater Philadelphia", "Greater Philadelphia")])
def test_get_city(city, expected):
    assert get_city(city) == expected


@pytest.mark.parametrize("company, expected", [("  Acme  ", "Acme"),
                                            ("", "Unknown company"),
                                            ("   ", "Unknown company")])
def test_clean_company(company, expected):
    assert clean_company(company) == expected
