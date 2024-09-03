def sum(number_1: float, number_2: float) -> float:
    if not isinstance(number_1, (int, float)) or not isinstance(number_2, (int, float)):
        raise TypeError("Invalid input type. Please provide a number.")
    
    result = number_1 + number_2
    #Overflow check
    if result == float('inf') or result == -float('inf'):
        raise OverflowError("Result is too large")
    return result

def subtract(number_1: float, number_2: float) -> float:
    return number_1 - number_2

def multiply(number_1: float, number_2: float) -> float:
    return number_1 * number_2

def divide(number_1: float, number_2: float) -> float:
    if number_1 == 0 or number_2 == 0:
        raise ValueError("Cannot divide by zero")
    
    return number_1 / number_2
    