import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize('input_text, expected_output',[
    ('hard', 'Hard'),
    ('help me', 'Help me'),
    ('pytest', 'Pytest')
])

def test_capitalize_positive(input_text, expected_output):
    assert string_utils.capitalize(input_text) == expected_output

@pytest.mark.negative
@pytest.mark.parametrize('input_text, expected_output',[
    ('123456qwerty', '123456qwerty'),
    ('', ''),
    ('   ', '   ')
])

def test_capitalize_negative(input_text, expected_output):
    assert string_utils.capitalize(input_text) == expected_output

@pytest.mark.positive
@pytest.mark.parametrize('input_text, expected_output',[
    (' go', 'go'),
    ('  wild', 'wild'),
    ('world', 'world'),
    ("", ""),
    (" a b c ", "a b c ")
])

def test_trim_positive(input_text, expected_output):
    assert string_utils.trim(input_text) == expected_output

@pytest.mark.negative
@pytest.mark.parametrize('input_text,expected_exception',[
    (None, AttributeError),
    (123, AttributeError),
    ([4,5], AttributeError)
])

def test_trim_negative(input_text, expected_exception):
    with pytest.raises(expected_exception):
        string_utils.trim(input_text)

@pytest.mark.positive
@pytest.mark.parametrize('input_text, symbol, expected',[
    ('House', 'H', True),
    ('Python', 'n', True),
    ('abc', '', True)
])

def test_contains_positive(input_text, symbol, expected):
    assert string_utils.contains(input_text, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize('input_text, symbol, expected',[
    ('World','n', False),
    ('One', 'w', False)
])

def test_contains_negative(input_text, symbol, expected):
    assert string_utils.contains(input_text, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize('input_text, symbol, expected',[
    ('Pytest', 'y', 'Ptest'),
    ('Pytest', 'Py', 'test'),
    ('SOS', 'S', 'O'),
    ('Pytest', 'w', 'Pytest')
])

def test_delete_symbol_positive(input_text, symbol,expected):
    result = string_utils.delete_symbol(input_text, symbol)
    assert result == expected

@pytest.mark.negative
@pytest.mark.parametrize('input_text, symbol, expected',[
    ('Test', "", "Test"),
    ('Z e r o', " ", "Zero"),
    ('aaa', 'a', ''),
])

def test_delete_symbol_negative(input_text, symbol, expected):
    result = string_utils.delete_symbol(input_text, symbol)
    assert result == expected