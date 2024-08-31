def single_roman_numeral_to_int(roman_numeral: str) -> int:
    roman_numerals_dict = get_roman_numerals_dict()

    capitalized_roman_numeral = capitalize_char(roman_numeral)
    
    roman_value = roman_numerals_dict[capitalized_roman_numeral]

    return roman_value
    
def capitalize_char(char: str) -> str:
    return char.upper()

def convert_roman_numerals_to_int_values(roman_numerals: str) -> list:
    roman_numerals_list = list(roman_numerals)
    roman_numerals_int_values = []
    
    for roman_numeral in roman_numerals_list:
        roman_numerals_int_values.append(single_roman_numeral_to_int(roman_numeral))
    
    return roman_numerals_int_values

def get_roman_numerals_dict() -> dict:
    roman_numerals_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    return roman_numerals_dict

def calculate_roman_numeral_value(roman_numeral_values: list[int]) -> int:
    roman_numeral_sum = 0
    n = len(roman_numeral_values)

    for i, value in enumerate(roman_numeral_values):
        if i + 1 < n and value < roman_numeral_values[i + 1]:
            roman_numeral_sum -= value
        else:
            roman_numeral_sum += value
    
    return roman_numeral_sum

def get_roman_numerals_sum(roman_numerals: str) -> int:
    roman_numeral_values = convert_roman_numerals_to_int_values(roman_numerals)
    roman_numeral_sum = calculate_roman_numeral_value(roman_numeral_values)
    
    return roman_numeral_sum