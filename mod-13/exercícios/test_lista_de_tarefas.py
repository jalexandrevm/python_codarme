from datetime import date, timedelta
import unittest

from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas


class TestAdicionarTarefa(unittest.TestCase):
    def setUp(self) -> None:
        self.tarefa1 = Tarefa("Estudar Java")
        self.tarefa2 = Tarefa("Estudar JavaScript")
        self.tarefa3 = Tarefa("Estudar TypeScript")
        self.lista = ListaDeTarefas()
    def test_adiciona_tarefa_a_lista_de_tarefas(self):
        self.assertEqual(len(self.lista), 0)
        self.lista.adicionar_tarefa(self.tarefa1)
        self.assertEqual(len(self.lista), 1)
        self.lista.adicionar_tarefa(self.tarefa2)
        self.assertEqual(len(self.lista), 2)
        self.lista.adicionar_tarefa(self.tarefa3)
        self.assertEqual(len(self.lista), 3)
        self.assertIn(self.tarefa1, self.lista.get_tarefas(True))
        self.assertIn(self.tarefa2, self.lista.get_tarefas(True))
        self.assertIn(self.tarefa3, self.lista.get_tarefas(True))

class TestGetTarefas(unittest.TestCase):
    def setUp(self) -> None:
        self.tarefa1 = Tarefa("Estudar Java")
        self.tarefa1.concluir()
        self.tarefa2 = Tarefa("Estudar JavaScript")
        self.tarefa3 = Tarefa("Estudar TypeScript")
        self.tarefa3.concluir()
        self.lista = ListaDeTarefas()
        self.lista.adicionar_tarefa(self.tarefa1)
        self.lista.adicionar_tarefa(self.tarefa2)
        self.lista.adicionar_tarefa(self.tarefa3)
    def test_retorna_lista_de_tarefas_adicionadas(self):
        self.assertIn(self.tarefa1, self.lista.get_tarefas(True))
        self.assertIn(self.tarefa2, self.lista.get_tarefas(True))
        self.assertIn(self.tarefa3, self.lista.get_tarefas(True))
    def test_tarefas_nao_concluidas(self):
        self.assertCountEqual(
            self.lista.get_tarefas(),
            [self.tarefa2]
        )
        pass

class TestGetTarefasAtrasadas(unittest.TestCase):
    def setUp(self) -> None:
        self.tarefa1 = Tarefa("Estudar Java")
        self.tarefa1.data = date.today()-timedelta(days=6)
        self.tarefa2 = Tarefa("Estudar JavaScript")
        self.tarefa2.data = date.today()+timedelta(days=3)
        self.tarefa3 = Tarefa("Estudar TypeScript")
        self.tarefa3.data = date.today()-timedelta(days=2)
        self.lista = ListaDeTarefas()
        self.lista.adicionar_tarefa(self.tarefa1)
        self.lista.adicionar_tarefa(self.tarefa2)
        self.lista.adicionar_tarefa(self.tarefa3)
    def test_tarefas_atrasadas(self):
        self.assertIn(self.tarefa1, self.lista.get_tarefas_atrasadas())
        self.assertIn(self.tarefa3, self.lista.get_tarefas_atrasadas())

class TestGetTarefasHoje(unittest.TestCase):
    def setUp(self) -> None:
        self.tarefa1 = Tarefa("Estudar Java")
        self.tarefa1.data = date.today()-timedelta(days=2)
        self.tarefa2 = Tarefa("Estudar JavaScript")
        self.tarefa2.data = date.today()+timedelta(days=3)
        self.tarefa3 = Tarefa("Estudar TypeScript")
        self.tarefa3.data = date.today()
        self.tarefa4 = Tarefa("Estudar SmallTalk")
        self.tarefa4.data = date.today()
        self.lista = ListaDeTarefas()
        self.lista.adicionar_tarefa(self.tarefa1)
        self.lista.adicionar_tarefa(self.tarefa2)
        self.lista.adicionar_tarefa(self.tarefa3)
        self.lista.adicionar_tarefa(self.tarefa4)
    def test_tarefas_hoje(self):
        self.assertIn(self.tarefa4, self.lista.get_tarefas_para_hoje())
        self.assertNotIn(self.tarefa2, self.lista.get_tarefas_para_hoje())
        self.assertCountEqual(
            self.lista.get_tarefas_para_hoje(),
            [self.tarefa4, self.tarefa3],
        )
        pass
    pass
unittest.main()
