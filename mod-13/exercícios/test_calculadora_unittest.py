from calculadora import somar, subtrair, multiplicar, dividir
import unittest

class TestSomar(unittest.TestCase):
    def test_soma_inteiros_positivos(self):
        soma = somar(3, 8)
        self.assertEqual(soma, 11)
    def test_soma_inteiros_negativos(self):
        soma = somar(-6, -2)
        self.assertEqual(soma, -8)
    def test_soma_inteiros_positivo_negativo(self):
        soma = somar(13, -22)
        self.assertEqual(soma, -9)
    def test_soma_inteiros_negativo_positivo(self):
        soma = somar(-6, 16)
        self.assertEqual(soma, 10)
    def test_soma_inteiros_zero_negativo(self):
        soma = somar(0, -7)
        self.assertEqual(soma, -7)
    def test_soma_inteiros_negativo_zero(self):
        soma = somar(-13, 0)
        self.assertEqual(soma, -13)
    def test_soma_inteiros_zero_positivo(self):
        soma = somar(0, 16)
        self.assertEqual(soma, 16)
    def test_soma_inteiros_positivo_zero(self):
        soma = somar(19, 0)
        self.assertEqual(soma, 19)
        pass
class TestDividir(unittest.TestCase):
    def test_dividi_inteiros_positivos(self):
        divisao = dividir(18, 6)
        self.assertEqual(divisao, 3)
    def test_dividi_inteiros_negativos(self):
        divisao = dividir(-8, -4)
        self.assertEqual(divisao, 2)
    def test_dividi_inteiros_positivo_negativo(self):
        divisao = dividir(12, -6)
        self.assertEqual(divisao, -2)
    def test_dividi_inteiros_negativo_positivo(self):
        divisao = dividir(-27, 3)
        self.assertEqual(divisao, -9)
    def test_dividi_inteiros_zero_negativo(self):
        divisao = dividir(0, -7)
        self.assertEqual(divisao, 0)
    def test_dividi_inteiros_negativo_zero(self):
        divisao = dividir(-13, 0)
        self.assertEqual(divisao, "Não é um número")
    def test_dividi_inteiros_zero_positivo(self):
        divisao = dividir(0, 15)
        self.assertEqual(divisao, 0)
    def test_dividi_inteiros_positivo_zero(self):
        divisao = dividir(24, 0)
        self.assertEqual(divisao, "Não é um número")
        pass
class TestMultiplicar(unittest.TestCase):
    def test_multiplica_inteiros_positivos(self):
        vezes = multiplicar(5, 6)
        self.assertEqual(vezes, 30)
    def test_multiplica_inteiros_negativos(self):
        vezes = multiplicar(-3, -7)
        self.assertEqual(vezes, 21)
    def test_multiplica_inteiros_positivo_negativo(self):
        vezes = multiplicar(11, -4)
        self.assertEqual(vezes, -44)
    def test_multiplica_inteiros_negativo_positivo(self):
        vezes = multiplicar(-4, 12)
        self.assertEqual(vezes, -48)
    def test_multiplica_inteiros_zero_negativo(self):
        vezes = multiplicar(0, -9)
        self.assertEqual(vezes, 0)
    def test_multiplica_inteiros_negativo_zero(self):
        vezes = multiplicar(-17, 0)
        self.assertEqual(vezes, 0)
    def test_multiplica_inteiros_zero_positivo(self):
        vezes = multiplicar(0, 11)
        self.assertEqual(vezes, 0)
    def test_multiplica_inteiros_positivo_zero(self):
        vezes = multiplicar(16, 0)
        self.assertEqual(vezes, 0)
        pass
class TestSubtrair(unittest.TestCase):
    def test_subtrai_inteiros_positivos(self):
        difere = subtrair(7, 2)
        self.assertEqual(difere, 5)
    def test_subtrai_inteiros_negativos(self):
        difere = subtrair(-9, -4)
        self.assertEqual(difere, -5)
    def test_subtrai_inteiros_positivo_negativo(self):
        difere = subtrair(17, -12)
        self.assertEqual(difere, 29)
    def test_subtrai_inteiros_negativo_positivo(self):
        difere = subtrair(-6, 16)
        self.assertEqual(difere, -22)
    def test_subtrai_inteiros_zero_negativo(self):
        difere = subtrair(0, -13)
        self.assertEqual(difere, 13)
    def test_subtrai_inteiros_negativo_zero(self):
        difere = subtrair(-5, 0)
        self.assertEqual(difere, -5)
    def test_subtrai_inteiros_zero_positivo(self):
        difere = subtrair(0, 14)
        self.assertEqual(difere, -14)
    def test_subtrai_inteiros_positivo_zero(self):
        difere = subtrair(17, 0)
        self.assertEqual(difere, 17)
        pass

class Testa_Calculadora(unittest.TestCase):
    def test_soma_numeros(self):
        self.assertEqual(somar(3, 9), 12, "passou")
    def test_subtrai_numeros(self):
        self.assertEqual(subtrair(3, 9), -6, "passou")
    def test_multiplica_numeros(self):
        self.assertEqual(multiplicar(3, 9), 27, "passou")
    def test_dividi_numeros(self):
        self.assertEqual(dividir(47, 5), 9.4, "passou")


unittest.main()
