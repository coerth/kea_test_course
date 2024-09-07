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

class TestCapitalizeChar:
    @pytest.mark.parametrize("input_char, expected_output", [
        ('a', 'A'),  # Lowercase alphabetic character
        ('z', 'Z'),  # Lowercase alphabetic character
        ('A', 'A'),  # Uppercase alphabetic character
        ('Z', 'Z'),  # Uppercase alphabetic character
        ('1', '1'),  # Non-alphabetic character
        ('@', '@'),  # Non-alphabetic character
        (' ', ' '),  # Non-alphabetic character
        
    ])
    def test_capitalize_char(self, input_char, expected_output):
        assert capitalize_char(input_char) == expected_output
    
    @pytest.mark.parametrize("input_char", [
        'ab',  # More than one character
        '',  # Empty string
    ])
    def test_capitalize_char_invalid_input(self, input_char):
        with pytest.raises(ValueError):
            capitalize_char(input_char)

class TestGetRomanNumeralsDict:
    def test_roman_numerals_dict_keys(self):
        # Act
        roman_numerals_dict = get_roman_numerals_dict()
        
        # Assert
        expected_keys = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
        assert set(roman_numerals_dict.keys()) == expected_keys
    
    def test_roman_numerals_dict_values(self):
        # Act
        roman_numerals_dict = get_roman_numerals_dict()
        
        # Assert
        expected_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        assert roman_numerals_dict == expected_values
    
    def test_roman_numerals_dict_no_unexpected_keys(self):
        # Act
        roman_numerals_dict = get_roman_numerals_dict()
        
        # Assert
        unexpected_keys = set(roman_numerals_dict.keys()) - {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
        assert not unexpected_keys

class TestSingleRomanNumeralToInt:
    @pytest.mark.parametrize("roman_numeral, expected_output", [
        ('I', 1), # Uppercase alphabetic characters
        ('V', 5), 
        ('X', 10),
        ('L', 50),
        ('C', 100), 
        ('D', 500), 
        ('M', 1000),
        ('i', 1),  # Lowercase alphabetic characters
        ('v', 5),  
        ('x', 10), 
        ('l', 50), 
        ('c', 100),  
        ('d', 500), 
        ('m', 1000),  
    ])
    def test_single_roman_numeral_to_int(self, roman_numeral, expected_output):
        assert single_roman_numeral_to_int(roman_numeral) == expected_output
    
    @pytest.mark.parametrize("roman_numeral", [
        'II',  # More than one character
        '',  # Empty string
    ])
    def test_single_roman_numeral_to_int_invalid_input_valuerror(self, roman_numeral):
        with pytest.raises(ValueError):
            single_roman_numeral_to_int(roman_numeral)
    
    @pytest.mark.parametrize("roman_numeral", [
        'A',  # Non-alphabetic character
        '1',  # Non-alphabetic character
        '@',  # Non-alphabetic character
    ])
    def test_single_roman_numeral_to_int_invalid_input_Keyerror(self, roman_numeral):
        with pytest.raises(KeyError):
            single_roman_numeral_to_int(roman_numeral)

class TestConvertRomanNumeralsToIntValues:
    @pytest.mark.parametrize("roman_numerals, expected_output", [
        ('IV', [1, 5]),  # Lowercase alphabetic characters
        ('IX', [1, 10]), 
        ('XL', [10, 50]), 
        ('XC', [10, 100]), 
        ('CD', [100, 500]), 
        ('CM', [100, 1000]), 
        ('iv', [1, 5]),  # Uppercase alphabetic characters
        ('ix', [1, 10]),  
        ('xl', [10, 50]),  
        ('xc', [10, 100]),  
        ('cd', [100, 500]),  
        ('cm', [100, 1000]),  
    ])
    def test_convert_roman_numerals_to_int_values(self, roman_numerals, expected_output):
        assert convert_roman_numerals_to_int_values(roman_numerals) == expected_output
    
    @pytest.mark.parametrize("roman_numerals", [
        '',  # More than one character
    ])
    def test_convert_roman_numerals_to_int_values_invalid_input_ValueError(self, roman_numerals):
        with pytest.raises(ValueError):
            convert_roman_numerals_to_int_values(roman_numerals)

    @pytest.mark.parametrize("roman_numerals", [
        'A',  # Non-alphabetic character
        '1',  # Non-alphabetic character
        '@',  # Non-alphabetic character
    ])
    def test_convert_roman_numerals_to_int_values_invalid_input_KeyError(self, roman_numerals):
        with pytest.raises(KeyError):
            convert_roman_numerals_to_int_values(roman_numerals)

class TestCalculateRomanNumeralValue:
    @pytest.mark.parametrize("roman_numeral_values, expected_output", [
        ([1], 1),  # Lower boundary
        ([100, 500], 400),  
        ([1000, 1000, 1000, 100, 1000, 10, 100, 1, 10], 3999),  # Upper boundary
    ])
    def test_calculate_roman_numeral_value_valid(self, roman_numeral_values, expected_output):
        assert calculate_roman_numeral_value(roman_numeral_values) == expected_output
    
    @pytest.mark.parametrize("roman_numeral_values", [
        [],  # Empty list
        [2],  # Invalid roman numeral
        [99999],  # Invalid roman numeral
    ])
    def test_calculate_roman_numeral_value_invalid_input_ValueError(self, roman_numeral_values):
        with pytest.raises(ValueError):
            calculate_roman_numeral_value(roman_numeral_values)

    @pytest.mark.parametrize("roman_numeral_values", [
        ['I'],  # Invalid type
        ['V'],  # Invalid type
        ['X'],  # Invalid type
        ['L', 1],
        ['1', '1'],
        ['1',1000]
    ])
    def test_calculate_roman_numeral_value_invalid_input_TypeError(self, roman_numeral_values):
        with pytest.raises(TypeError):
            calculate_roman_numeral_value(roman_numeral_values)

class TestGetRomanNumeralsSum:
    @pytest.mark.parametrize("roman_numerals, expected_output", [
        ('I', 1),  # Lower boundary
        ('i', 1),
        ('CM', 900),  
        ('cm', 900),  
        ('MMMCMXCIX', 3999),  # Upper boundary
        ('mmmcmxcix', 3999),
    ])
    def test_get_roman_numerals_sum(self, roman_numerals, expected_output):
        assert get_roman_numerals_sum(roman_numerals) == expected_output
    
    @pytest.mark.parametrize("roman_numerals", [
        '',  # Empty string
        'MMMMMMMMM'
    ])
    def test_get_roman_numerals_sum_invalid_input_valueerror(self, roman_numerals):
        with pytest.raises(ValueError):
            get_roman_numerals_sum(roman_numerals)

    @pytest.mark.parametrize("roman_numerals", [
        'A',  # Non-alphabetic character
        '1',  # Non-alphabetic character
        '@',  # Non-alphabetic character
    ])
    def test_get_roman_numerals_sum_invalid_input_KeyError(self, roman_numerals):
        with pytest.raises(KeyError):
            get_roman_numerals_sum(roman_numerals)

    
    