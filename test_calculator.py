import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(3, 5) == 8
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 5) == -4
    assert calc.subtract(-5, -3) == -2
    
def test_multiply():
    calc = Calculator()
    assert calc.multiply(3.0, 4.0) == (12)  
    assert calc.multiply(3, -5) == -15 
    assert calc.multiply(3, 5) == 15  
    

def test_divide():
    calc = Calculator()
    assert calc.divide(12, 3) == 4  
    assert calc.divide(7, 2) == 3.5  
    assert calc.divide(12, 0) == float('inf')  

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])

def test_add_parameterized(calculator,a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, -2),
    (-1, 1, -2),
    (-1, -1, 0),
    (0, 0, 0)
])

def test_subtract_parameterized(calculator,a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 15),
    (-1, 1, -1),
    (-1, -1, 1),
    (0, 0, 0)
])

def test_multiply_parameterized(calculator,a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (-1, 1, -1),
    (-20, -4, 5),
    (0, 10, 0)
])

def test_divide_parameterized(calculator,a, b, expected):
    assert calculator.divide(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (2, -2, 0.25),
    (1, 100, 1),
    (10, 0, 1)
])

def test_power_parameterized(calculator,a, b, expected):
    assert calculator.power(a, b) == expected

@pytest.mark.parametrize("a, expected", [
    (0,1),
    (1,1),
    (-1, -2),
    (5,120)
])

def test_factorial_parameterized(calculator, a, expected):
    if a < 0:
        with pytest.raises(ValueError):
            calculator.factorial(a)
    else:
        assert calculator.factorial(a) == expected

@pytest.mark.parametrize("n, expected, raises", [
    (0, 0, None),       # fib(0) = 0
    (1, 1, None),       # fib(1) = 1
    (7, 13, None),      # fib(7) = 13
    (10, 55, None),     # fib(10) = 55
    (-1, None, ValueError),  # Should raise ValueError
])
def test_fibonacci_parameterized(calculator, n, expected, raises):
    if raises:
        with pytest.raises(raises):
            calculator.fibonacci(n)
    else:
        assert calculator.fibonacci(n) == expected
def test_precise_addition(precise_calculator):
    # Test with default precision of 2
    assert precise_calculator.add(2.7145, 3.145698) == 5.86  # 2.7145 + 3.145698 = 5.860198 → 5.86
    assert precise_calculator.add(0.3, 2.4) == 2.7  # 0.3 + 2.4 = 2.7 → 2.7

@pytest.mark.parametrize("a, b, expected", [
    (1.2345, 2.3456, 3.58),  # 1.2345 + 2.3456 = 3.5801 → 3.58 (precision 2)
    (0.1, 0.2, 0.3),         # 0.1 + 0.2 = 0.3 → 0.3
    (5.5555, 4.4444, 10.0)   # 5.5555 + 4.4444 = 9.9999 → 10.0
])
def test_addition_precision(precise_calculator, a, b, expected):
    assert precise_calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, precision, expected", [
    (1.2345, 2.3456, 2, 3.58),   # precision 2
    (1.2345, 2.3456, 4, 3.5801), # precision 4
    (0.1, 0.2, 1, 0.3),         # precision 1
])
def test_variable_precision_addition(calculator_with_precision, a, b, precision, expected):
    if calculator_with_precision.precision == precision:
        assert calculator_with_precision.add(a, b) == expected