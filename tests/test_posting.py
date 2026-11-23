from posting import Posting

def test_city():
    posting = Posting("ML Engineer", "Acme AI Labs", "Lisbon, Portugal")
    assert posting.city() == "Lisbon"


def test_annual_salary_hourly():
    posting = Posting("ML Engineer", "Acme AI Labs", "Lisbon, Portugal", "50.0", "HOURLY")
    assert posting.annual_salary() == 104000.0


def test_annual_salary_missing():
    posting = Posting("AI Engineer", "Robo Inc", "Braga, Portugal")
    assert posting.annual_salary() is None


def test_summary_without_salary():
    posting = Posting("AI Engineer", "Robo Inc", "Braga, Portugal")
    assert posting.summary().endswith("salary not available")