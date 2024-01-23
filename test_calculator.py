import pytest
from app.calculator import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_multiply_positive(self):
        assert self.calc.multiply(2, 3) == 6

    def test_division_positive(self):
        assert self.calc.division(6, 2) == 3

    def test_subtraction_positive(self):
        assert self.calc.subtraction(5, 2) == 3

    def test_adding_positive(self):
        assert self.calc.adding(2, 3) == 5
