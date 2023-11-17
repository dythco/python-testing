import pytest
from testing.basic import parser

# Test case with default delimiter and no transform function
def test_parser_default_delimiter_no_transform():
    data = "apple,banana,orange"
    result = parser(data)
    assert result == ["apple", "banana", "orange"]

# Test case with a custom delimiter and no transform function
def test_parser_custom_delimiter_no_transform():
    data = "apple;banana;orange"
    result = parser(data, delimiter=";")
    assert result == ["apple", "banana", "orange"]

# Test case with default delimiter and a transform function
def test_parser_default_delimiter_with_transform():
    data = "1,2,3"
    transform_func = lambda x: int(x)
    result = parser(data, transform=transform_func)
    assert result == [1, 2, 3]

# Test case with custom delimiter and a transform function
def test_parser_custom_delimiter_with_transform():
    data = "1|2|3"
    transform_func = lambda x: int(x)
    result = parser(data, delimiter="|", transform=transform_func)
    assert result == [1, 2, 3]

# Test case with default delimiter and transform function converting to uppercase
def test_parser_default_delimiter_transform_to_uppercase():
    data = "apple,banana,orange"
    transform_func = lambda x: x.upper()
    result = parser(data, transform=transform_func)
    assert result == ["APPLE", "BANANA", "ORANGE"]

# Test case with default delimiter and transform function converting to lowercase
def test_parser_default_delimiter_transform_to_lowercase():
    data = "APPLE,BANANA,ORANGE"
    transform_func = lambda x: x.lower()
    result = parser(data, transform=transform_func)
    assert result == ["apple", "banana", "orange"]

# Test case with default delimiter and transform function applying a custom transformation
def test_parser_default_delimiter_custom_transform():
    data = "1,2,3"
    transform_func = lambda x: f"Value: {x}"
    result = parser(data, transform=transform_func)
    assert result == ["Value: 1", "Value: 2", "Value: 3"]

# Additional test case with special characters and default delimiter
"""
def test_parser_special_characters_default_delimiter():
    data = "!@#$%^&*(),.;:{}[]"
    result = parser(data)
    expected_result = ['!@#$%^&*()', '', '', '', '', '', '', '', '', '', '', '', '', '', ';', '', ':', '{', '}', '']
    assert result == expected_result
"""