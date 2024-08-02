import pytest 
from conta_bancaria import ContaBancaria


@pytest.fixture
def banco():
    return ContaBancaria("Ezequiel", 10)
def test_depositar(banco):
    assert banco.depositar(5) == 5
    assert banco.obter_saldo() == 15
def test_sacar(banco):
    assert banco.sacar(5) == 5
    assert banco.obter_saldo() == 5
def test_obter_titular(banco):
    assert banco.obter_titular() == "Ezequiel"