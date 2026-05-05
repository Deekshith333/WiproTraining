from operator import ne

import pytest

from src.calculations import *
from src.calculations import calculations

class TestCalculations:
#     @pytest.fixture()
# def setUp(self):
    calc = calculations()

    @pytest.mark.parametrize("n1, n2, exval", [(5, 5, 10), (-5, -5, -10), (0, 5, 5)])
def test_add(self, n1, n2, exval):
    res = self.calc.add(n1, n2)
    assert res == exval, 'Addition Err'




# def test_add(self):
#     res = self.calc.add(10, 5)
#     assert res == 15, 'Addition Err'

def test_sub(self):
    res = self.calc.sub(10, 5)
    assert res == 5, 'Subtraction Err'

def test_mul(self):
    res = self.calc.mul(10, 5)
    assert res == 50, 'Multiplication Err'

def test_div(self):
    res = self.calc.div(10, 5)
    assert res == 2.0, 'Division Err'





def test_ne():
    res = ne(10, 5)
    assert res == True, 'NE'

    def test_diverr():
        with pytest.raises(ZeroDivisionError):
            diverr(10,0)