import pytest

from roman_numeral import capitalize_char, single_roman_numeral_to_int, convert_roman_numerals_to_int_values, get_roman_numerals_dict, calculate_roman_numeral_value, get_roman_numerals_sum

# Test for the roman_numeral module

class TestRomanNumeralSingleRomanNumeralToInt:
    def test_single_roman_numeral_to_int_positive(self):
        # Arrange
        roman_numeral = 'i'
        expected = 1
        
        # Act
        result = single_roman_numeral_to_int(roman_numeral)
        
        # Assert
        assert result == expected

    def test_single_roman_numeral_to_int_negative(self):
        # Arrange
        roman_numeral = 'i'
        expected = 2
        
        # Act
        result = single_roman_numeral_to_int(roman_numeral)
        
        # Assert
        assert result != expected

class TestRomanNumeralCapitalizeChar:
    def test_capitalize_char_positive(self):
        # Arrange
        char = 'i'
        expected = 'I'
        
        # Act
        result = capitalize_char(char)
        
        # Assert
        assert result == expected

    def test_capitalize_char_negative(self):
        # Arrange
        char = 'i'
        expected = 'i'
        
        # Act
        result = capitalize_char(char)
        
        # Assert
        assert result != expected

class TestRomanNumeralConvertRomanNumeralsToIntValues:
    def test_convert_roman_numerals_to_int_values_positive(self):
        # Arrange
        roman_numerals = 'IV'
        expected = [1, 5]
        
        # Act
        result = convert_roman_numerals_to_int_values(roman_numerals)
        
        # Assert
        assert result == expected

    def test_convert_roman_numerals_to_int_values_negative(self):
        # Arrange
        roman_numerals = 'IV'
        expected = [1, 4]
        
        # Act
        result = convert_roman_numerals_to_int_values(roman_numerals)
        
        # Assert
        assert result != expected

class TestRomanNumeralGetRomanNumeralsDict:
    def test_get_roman_numerals_dict_positive(self):
        # Arrange
        expected = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        # Act
        result = get_roman_numerals_dict()
        
        # Assert
        assert result == expected

    def test_get_roman_numerals_dict_negative(self):
        # Arrange
        expected = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 100,
        }
        
        # Act
        result = get_roman_numerals_dict()
        
        # Assert
        assert result != expected

class TestRomanNumeralCalculateRomanNumeralValue:
    def test_calculate_roman_numeral_value_positive(self):
        # Arrange
        roman_numeral_values = [1, 5]
        expected = 4
        
        # Act
        result = calculate_roman_numeral_value(roman_numeral_values)
        
        # Assert
        assert result == expected

    def test_calculate_roman_numeral_value_negative(self):
        # Arrange
        roman_numeral_values = [1, 5]
        expected = 6
        
        # Act
        result = calculate_roman_numeral_value(roman_numeral_values)
        
        # Assert
        assert result != expected

class TestRomanNumeralGetRomanNumeralsSum:
    def test_get_roman_numerals_sum_positive(self):
        # Arrange
        roman_numerals = 'IV'
        expected = 4
        
        # Act
        result = get_roman_numerals_sum(roman_numerals)
        
        # Assert
        assert result == expected

    def test_get_roman_numerals_sum_negative(self):
        # Arrange
        roman_numerals = 'IV'
        expected = 5
        
        # Act
        result = get_roman_numerals_sum(roman_numerals)
        
        # Assert
        assert result != expected


# Parameterized tests

@pytest.mark.parametrize(
    'roman_numeral, expected',
    [
        ('i', 1),
        ('v', 5),
        ('x', 10),
        ('l', 50),
        ('c', 100),
        ('d', 500),
        ('m', 1000),
    ]
)
def test_single_roman_numeral_to_int_parameterized(roman_numeral, expected):
    result = single_roman_numeral_to_int(roman_numeral)
    assert result == expected

@pytest.mark.parametrize(
    'char, expected',
    [
        ('i', 'I'),
        ('v', 'V'),
        ('x', 'X'),
        ('l', 'L'),
        ('c', 'C'),
        ('d', 'D'),
        ('m', 'M'),
    ]
)
def test_capitalize_char_parameterized(char, expected):
    result = capitalize_char(char)
    assert result == expected

@pytest.mark.parametrize(
    'roman_numerals, expected',
    [
        ('IV', [1, 5]),
        ('IX', [1, 10]),
        ('XL', [10, 50]),
        ('XC', [10, 100]),
        ('CD', [100, 500]),
        ('CM', [100, 1000]),
    ]
)
def test_convert_roman_numerals_to_int_values_parameterized(roman_numerals, expected):
    result = convert_roman_numerals_to_int_values(roman_numerals)
    assert result == expected

@pytest.mark.parametrize(
    'roman_numeral_values, expected',
    [
        ([1, 5], 4),
        ([1, 10], 9),
        ([10, 50], 40),
        ([10, 100], 90),
        ([100, 500], 400),
        ([100, 1000], 900),
    ]
)
def test_calculate_roman_numeral_value_parameterized(roman_numeral_values, expected):
    result = calculate_roman_numeral_value(roman_numeral_values)
    assert result == expected

@pytest.mark.parametrize(
    'roman_numerals, expected',
    [
        ('IV', 4),
        ('IX', 9),
        ('XL', 40),
        ('XC', 90),
        ('CD', 400),
        ('CM', 900),
    ]
)
def test_get_roman_numerals_sum_parameterized(roman_numerals, expected):
    result = get_roman_numerals_sum(roman_numerals)
    assert result == expected