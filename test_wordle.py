import pytest
from functions import word_entered, contains_illegal_letter

# TEST 1

# This tests one of the main features of the application, notably the user's ability to enter each of their 5-letter Wordle guesses as an input for Python to process.
# The test cases have been written to test if the user is asked to re-enter their word if it does not meet the requirements.

# Test case 1 - the expected result is "Pass" as the input provided to Pytest is a 5-letter alphabetic word that will be returned by the function in lowercase.
def test_word_entered(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "START")
    assert word_entered() == "start"

# Test case 2 - the expected result is "Pass" as typing "q" should present the user with the KeyboardInterrupt error and quit the program
    monkeypatch.setattr('builtins.input', lambda _: "q")
    with pytest.raises(KeyboardInterrupt):
        word_entered()

# TEST 2

# This tests another one of the main features of the application, notably the user's ability to enter a coded input that represents the feedback given to them at the NY website.
# The test cases have been written to ensure that the user is asked to re-enter their code in an XGY-syntax only.

# Test cases 1-3 - the expected result for each is "Pass" as the input provided to Pytest contains a non-permitted character
def test_contains_illegal_letter():
    assert contains_illegal_letter("XYGXA") == True
    assert contains_illegal_letter("QWERT") == True
    assert contains_illegal_letter("1GGGG") == True

# Test case 4 - the expected result is "Pass" as the input provided to Pytest contains allowed characters only.
    assert contains_illegal_letter("GYXGY") == False