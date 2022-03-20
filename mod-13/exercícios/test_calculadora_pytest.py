import pytest
from calculadora import somar, subtrair, multiplicar, dividir


class Testa_Calculadora:
    # @pytest.fixture
    # def a(self):
    #     return self.a

    @pytest.mark.parametrize("a,b,result", [
        (3, 5, 8),
        (-9, 5, -4),
        (0, 5, 5),
        (-9, -15, -24),
        (0, -35, -35)
    ])
    def test_soma_numeros(self, a, b, result):
        assert somar(a, b) == (result)

    @pytest.mark.parametrize("a,b,result", [
        (3, 5, -2),
        (-9, 5, -14),
        (0, 5, -5),
        (-9, -15, 6),
        (0, -35, 35)
    ])
    def test_subtrai_numeros(self, a, b, result):
        assert subtrair(a, b) == (result)

    @pytest.mark.parametrize("a,b,result", [
        (3, 5, 15),
        (-9, 5, -45),
        (0, 5, 0),
        (-9, -15, 135),
        (-35, 0, 0)
    ])
    def test_multiplica_numeros(self, a, b, result):
        assert multiplicar(a, b) == (result)

    @pytest.mark.parametrize("a,b,result", [
        (3, 5, 0.6),
        (-9, 5, -1.8),
        (5, 0, "Não é um número"),
        (-9, -15, 0.6),
        (0, -35, 0)
    ])
    def test_dividi_numeros(self, a, b, result):
        assert dividir(a, b) == (result)
