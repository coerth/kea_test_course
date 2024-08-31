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

