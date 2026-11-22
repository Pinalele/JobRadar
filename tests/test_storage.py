import pytest
from posting import Posting
from storage import load_postings, save_postings


@pytest.fixture
def sample_postings():
    return [
        Posting("ML Engineer", "Acme AI Labs", "Lisbon, Portugal", "50.0", "HOURLY"),
        Posting("Data Scientist", "DataCo", "Porto, Portugal", "3000.0", "MONTHLY"),
    ]

def test_save_and_load_postings(tmp_path, sample_postings):
    path = tmp_path / "postings.json"
    save_postings(sample_postings, path)
    loaded = load_postings(path)
    assert loaded == sample_postings
