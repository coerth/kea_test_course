import pytest
from calculator_exercise_unit_tests.calculator import sum, subtract, multiply, divide

# Test for the calculator module

class TestCalculatorSum:
    def test_add_positive(self):
        # Arrange
        a = 1
        b = 2
        expected = 3
        
        # Act
        result = sum(a, b)
        
        # Assert
        assert result == expected

    def test_add_negative(self):
        # Arrange
        a = -1
        b =  2
        expected = -3
        
        # Act
        result = sum(a, b)
        
        # Assert
        assert result != expected

class TestCalculatorSubtract:

    def test_subtract_positive(self):
        # Arrange
        a = 1
        b = 2
        expected = -1
        
        # Act
        result = subtract(a, b)
        
        # Assert
        assert result == expected

    def test_subtract_negative(self):
        # Arrange
        a = -1
        b = 3
        expected = 1
        
        # Act
        result = subtract(a, b)
        
        # Assert
        assert result != expected

class TestCalculatorMultiply:
    
        def test_multiply_positive(self):
            # Arrange
            a = 1
            b = 2
            expected = 2
            
            # Act
            result = multiply(a, b)
            
            # Assert
            assert result == expected
    
        def test_multiply_negative(self):
            # Arrange
            a = -1
            b = -4
            expected = 2
            
            # Act
            result = multiply(a, b)
            
            # Assert
            assert result != expected

class TestCalculatorDivide:
        
            def test_divide_positive(self):
                # Arrange
                a = 4
                b = 2
                expected = 2
                
                # Act
                result = divide(a, b)
                
                # Assert
                assert result == expected
        
            def test_divide_negative(self):
                # Arrange
                a = 4
                b = 2
                expected = 3
                
                # Act
                result = divide(a, b)
                
                # Assert
                assert result != expected