import pytest

from calculator import Calculator
@pytest.fixture

def calculator():
    return Calculator()

import pytest
from calculator import Calculator

class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision
    
    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result
    
    def multiply(self, a, b):
        result = super().multiply(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

@pytest.fixture
def precise_calculator():
    return PreciseCalculator(precision=2)

@pytest.fixture(params=[0, 2, 4])
def calculator_with_precision(request):
    return PreciseCalculator(precision=request.param)