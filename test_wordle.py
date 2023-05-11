import pytest
from wordle import word_entered

# TEST 1

def test_word_entered(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "ALERT")
    assert word_entered() == "alert"