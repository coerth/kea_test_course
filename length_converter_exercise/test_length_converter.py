import pytest
from length_converter import LengthConverter

class TestLengthConverterValid:
        
        @pytest.mark.parametrize("value, metric, expected", [
            (1, 'Metric', 2.54),
            (1, 'Imperial', 0.39370078740157477),
            (0, 'Metric', 0),
            (0, 'Imperial', 0),
            (-1, 'Metric', 2.54),
            (-1, 'Imperial', 0.39370078740157477),
            (float('inf'), 'Metric', float('inf')),
            (float('inf'), 'Imperial', float('inf')),
            (float('-inf'), 'Metric', float('inf')),
            (float('-inf'), 'Imperial', float('inf')),
        ])
        def test_convert_to_chosen_metric(self, value, metric, expected):
            # Arrange
            length_converter = LengthConverter(value, metric)
            
            # Act
            result = length_converter.convert_to_chosen_metric()
            
            # Assert
            assert result == expected

class TestLengthConverterInvalid:
    @pytest.mark.parametrize("value, metric, expected_exception", [
        ('1', 'Metric', TypeError),  # Invalid value type
        (1, 'metric', ValueError),  # Invalid metric
        (1, 'invalid', ValueError),  # Invalid metric
        (1, 1, ValueError),  # Invalid metric type
        (1, None, ValueError),  # Invalid metric type
        (None, 'Metric', TypeError),  # Invalid value type
        (None, None, TypeError),  # Invalid value type
    ])
    def test_invalid_metric(self, value, metric, expected_exception):
        with pytest.raises(expected_exception):
            LengthConverter(value, metric)