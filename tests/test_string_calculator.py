import pytest
from src.string_calculator import add

def test_add_empty_string():
    assert add("") == 0

def test_add_single_number():
    assert add("1") == 1

def test_add_two_numbers():
    assert add("1,5") == 6

def test_add_multiple_numbers():
    assert add("1,2,3") == 6

def test_add_newline_delimiter():
    assert add("1\n2,3") == 6

def test_add_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_add_negative_numbers():
    with pytest.raises(ValueError) as exc_info:
        add("1,-2,3")
    assert str(exc_info.value) == "negative numbers not allowed: -2"

def test_add_multiple_negative_numbers():
    with pytest.raises(ValueError) as exc_info:
        add("1,-2,-3")
    assert str(exc_info.value) == "negative numbers not allowed: -2, -3"