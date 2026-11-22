from cleaning import clean_title, to_annual_salary

def test_clean_title_removes_extra_spaces():
    assert clean_title("  data scientist  ") == "Data Scientist"


def test_clean_title_capitalises_each_word():
    assert clean_title("machine learning ENGINEER") == "Machine Learning Engineer"

def test_clean_title_keeps_apostrophes():
    assert clean_title("women's business center") == "Women's Business Center"

def test_clean_title_keeps_acronyms():
    assert clean_title("ai engineer") == "AI Engineer"


def test_to_annual_salary_same():
    assert to_annual_salary("65000.0", "YEARLY") == 65000.0

def test_to_annual_salary_plus_14():
    assert to_annual_salary("3000.0", "MONTHLY") == 42000.0

def test_to_annual_salary_same_hourly_2080():
    assert to_annual_salary("50.0", "HOURLY") == 104000.0

def test_to_annual_salary_same_unknown_period():
    assert to_annual_salary("900.0", "WEEKLY") is None

def test_to_annual_salary_same_empty_salary():
    assert to_annual_salary("", "YEARLY") is None

def test_to_annual_salary_same_invalid_salary():
    assert to_annual_salary("$3,000", "MONTHLY") is None
