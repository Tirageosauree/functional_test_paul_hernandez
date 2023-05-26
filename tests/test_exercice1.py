import pytest
from exercice1 import Calculator

def test_calculator_init():
    calc = Calculator()
    assert calc.get_memory() == 0

def test_calculator_addition():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.get_memory() == 3

def test_calculator_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.get_memory() == 2

def test_calculator_multiplication():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.get_memory() == 6

def test_calculator_division():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.get_memory() == 3

def test_calculator_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(6, 0)

def test_calculator_power():
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.get_memory() == 8

def test_calculator_sqrt():
    calc = Calculator()
    assert calc.sqrt(9) == 3
    assert calc.get_memory() == 3

def test_calculator_sqrt_negative():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        calc.sqrt(-1)

def test_calculator_clear_memory():
    calc = Calculator()
    calc.add(1, 2)
    calc.clear_memory()
    assert calc.get_memory() == 0
