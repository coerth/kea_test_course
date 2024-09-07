class LengthConverter():
    VALID_METRICS = ['Metric', 'Imperial']
    INCH_CM = 2.54

    def __init__(self, value: float, metric: str):

        if not isinstance(value, (int, float)):
            raise TypeError('Input must be a number')

        if metric not in self.VALID_METRICS:
            raise ValueError('Invalid metric')

        self.value = abs(value)
        self.metric = metric
        
    def convert_to_chosen_metric(self) -> float:

        if self.metric == 'Metric':
            return self.value * self.INCH_CM
        else:
            return self.value / self.INCH_CM
        
    