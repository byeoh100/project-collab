from roman_numerals import to_roman
import pytest

def test_one():
    assert to_roman(1) == "I"

def test_four():
    assert to_roman(4) == "IV"

def test_eight():
    assert to_roman(8) == "VIII"

def test_nine():
    assert to_roman(9) == "IX"