"""HW1 Question 3 Tests"""

import sys

sys.path.append('.')
from src.q3 import capitalize_words


"""Please write your tests here."""
def base_case() -> None:
    """Tests whether or not it capitalizes the first letter of each word"""
    assert capitalize_words("hello cs2100") == "Hello Cs2100"

def second_case() -> None:
    """Tests one word """
    assert capitalize_words("hello") == "Hello"

def third_case() -> None:
    """Tests when the first letter in the first word is already capitalized"""
    assert capitalize_words("Hello king") == "Hello King"

def fourth_case() -> None:
    """Tests when the first letter int he second word is capitalized"""
    assert capitalize_words("hello Everyone") == "Hello Everyone"

def fifth_case() -> None:
    """Tests mix of uppercase and lowercase letters after the first one"""
    assert capitalize_words("hELlo pEoPlE") == "HELlo PEoPlE"

def sixth_case() -> None:
    """Tests strings with multiple spaces"""
    assert capitalize_words("hello   everyone ") == "Hello   Everyone"

def seventh_case() -> None:
    """Tests strings with punctuation/ other characters before first letter"""
    assert capitalize_words(" .Hello #everyone") == ".Hello #Everyone"

def eighth_case() -> None:
    """Tests an empty string"""
    assert capitalize_words("") == ""

def ninth_case() -> None:
    """Tests numbers at the beginning"""
    assert capitalize_words("3hello 7Again") == "3Hello 7Again"
