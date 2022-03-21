from calculadora_de_notas import Aluno, Turma, CalculadoraDeNotas
import unittest

class TestAluno(unittest.TestCase):
    def setUp(self) -> None:
        self.aluno1 = Aluno("pedro", 7.5)
        self.aluno2 = Aluno("victor", 9)
        self.aluno3 = Aluno("cisco", 3)
        self.aluno4 = Aluno("jonas", 0.5)
        self.aluno5 = Aluno("brena", 10)
        self.aluno6 = Aluno("livia", 9.5)
    def test_retorna_nome(self):
        self.assertEqual(self.aluno1.get_nome(), "pedro")
        self.assertEqual(self.aluno5.get_nome(), "brena")
        self.assertEqual(self.aluno6.get_nome(), "livia")
    def test_retorna_nota(self):
        self.assertEqual(self.aluno2.get_nota(), 9)
        self.assertEqual(self.aluno3.get_nota(), 3)
        self.assertEqual(self.aluno4.get_nota(), 0.5)
    pass
class TestTurmaAdicionaAluno(unittest.TestCase):
    def setUp(self) -> None:
        self.aluno1 = Aluno("pedro", 7.5)
        self.aluno2 = Aluno("victor", 9)
        self.aluno3 = Aluno("cisco", 3)
        self.aluno4 = Aluno("jonas", 0.5)
        self.turma1 = Turma()
    def test_adiciona_aluno_turma(self):
        self.assertEqual(self.turma1.get_qtd_alunos(), 0)
        self.turma1.add_aluno(self.aluno1)
        self.assertEqual(self.turma1.get_qtd_alunos(), 1)
        self.turma1.add_aluno(self.aluno2)
        self.assertEqual(self.turma1.get_qtd_alunos(), 2)
        self.turma1.add_aluno(self.aluno3)
        self.assertEqual(self.turma1.get_qtd_alunos(), 3)
        self.turma1.add_aluno(self.aluno4)
        self.assertEqual(self.turma1.get_qtd_alunos(), 4)
        self.assertIn(self.aluno3, self.turma1.get_alunos())
        self.assertIn(self.aluno2, self.turma1.get_alunos())

class TestTurmaNotaAprovacao(unittest.TestCase):
    def setUp(self) -> None:
        self.aluno1 = Aluno("pedro", 7.5)
        self.aluno2 = Aluno("victor", 9)
        self.turma2 = Turma()
    def test_define_nota_aprova(self):
        self.assertLessEqual(
            self.turma2.get_nota_aprovacao(),
            10,
        )
        self.turma2.set_nota_aprovacao(7)
        self.assertLessEqual(
            self.turma2.get_nota_aprovacao(),
            7,
        )
        self.turma2.set_nota_aprovacao(5)
        self.assertLessEqual(
            self.turma2.get_nota_aprovacao(),
            6,
        )
        self.turma2.set_nota_aprovacao(9)
        self.assertGreaterEqual(
            self.turma2.get_nota_aprovacao(),
            6,
        )
    pass

class TestTurmaRetornaAluno(unittest.TestCase):
    def setUp(self) -> None:
        self.aluno1 = Aluno("pedrito", 7.5)
        self.aluno2 = Aluno("vilma", 9)
        self.aluno3 = Aluno("francisco", 3)
        self.aluno4 = Aluno("joana", 0.5)
        self.aluno5 = Aluno("tiana", 8.5)
        self.turma3 = Turma()
        self.turma3.add_aluno(self.aluno1)
        self.turma3.add_aluno(self.aluno2)
        self.turma3.add_aluno(self.aluno3)
        self.turma3.add_aluno(self.aluno4)
        self.turma3.add_aluno(self.aluno5)
    def test_verifica_alunos(self):
        self.assertIn(self.aluno2, self.turma3.get_alunos())
        self.assertIn(self.aluno3, self.turma3.get_alunos())
    def test_quantidade_alunos(self):
        for it in self.turma3.get_alunos():
            print(it.get_nome())
        self.assertEqual(self.turma3.get_qtd_alunos(), 4)
        pass
    pass

unittest.main()
