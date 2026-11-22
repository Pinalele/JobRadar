from cleaning import clean_title

def test_clean_title_removes_extra_spaces():
    assert clean_title("  data scientist  ") == "Data Scientist"


def test_clean_title_capitalises_each_word():
    assert clean_title("machine learning ENGINEER") == "Machine Learning Engineer"

def test_clean_title_keeps_apostrophes():
    assert clean_title("women's business center") == "Women's Business Center"

def test_clean_title_keeps_acronyms():
    assert clean_title("ai engineer") == "AI Engineer"