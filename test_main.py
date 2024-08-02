import pytest 
from main import Calculadora

@pytest.fixture
def calc():
    return Calculadora()
def test_soma(calc):
    assert calc.soma(10,5) == 15
def test_subtracao(calc):
    assert calc.subtracao(10,5) == 5

