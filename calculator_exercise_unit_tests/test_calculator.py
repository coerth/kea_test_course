import pytest
import sys
from calculator_exercise_unit_tests.calculator import sum, subtract, multiply, divide


# Test for the calculator module

# Initial tests
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

# More comprehensive tests

class TestExtendedCalculatorSum:

    @pytest.mark.parametrize("a, b, expected", [
        (sys.float_info.min, sys.float_info.min, sys.float_info.min + sys.float_info.min),  # Lower boundary
        (sys.float_info.max, 0.01, sys.float_info.max + 0.01),  # Upper boundary
        (50.5, 50.5, 50.5 + 50.5)  # Middle boundary
    ])
    def test_sum_valid_boundaries(self, a, b, expected):
        # Act
        result = sum(a, b)
        
        # Assert
        assert result == expected
     
    def test_sum_boundary_zero(self):
         # Arrange
         a = 0
         b = 0
         expected = 0
         
         # Act
         result = sum(a, b)
         
         # Assert
         assert result == expected
    
    @pytest.mark.parametrize("a, b", [
        (sys.float_info.max, sys.float_info.max),  # Upper boundary
        (-sys.float_info.max, -sys.float_info.max)  # Lower boundary
    ])
    def test_sum_invalid_boundary(self, a, b):
        with pytest.raises(OverflowError):
            sum(a, b)
    
    @pytest.mark.parametrize("a, b", [
        ('a', 2),  # Invalid type
        (2, 'b'),  # Invalid type
        ('a', 'b')  # Invalid type
    ])
    def test_sum_invalid_type(self, a, b):
        with pytest.raises(TypeError):
            sum(a, b)