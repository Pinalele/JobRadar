import json
from dataclasses import asdict

from posting import Posting

def save_postings(postings, path):
    """Save a list of Posting objects to a JSON file."""
    ai_posting_dicts = [asdict(posting) for posting in postings]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(ai_posting_dicts, f, indent=2)


def load_postings(path):
    """Load Posting objects from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        posting_dicts = json.load(f)
    return [Posting(**d) for d in posting_dicts]