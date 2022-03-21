from datetime import datetime, timedelta
from tarefa import Tarefa
import unittest

class TestTarefa(unittest.TestCase):
  def setUp(self) -> None:
    self.tarefa = Tarefa("Estudar JavaScript")
  def test_tarefa_concluida(self):
    tarefa = Tarefa("Estudar Python")
    tarefa.concluir()
    self.assertEqual(tarefa.concluida, True)
  def test_tarefa_concluida_verdade(self):
    tarefa = Tarefa("Estudar Java")
    tarefa.concluir()
    self.assertTrue(tarefa.concluida)
  def test_tarefa_criada(self):
    # tarefa = Tarefa("Estudar Django")
    self.assertFalse(self.tarefa.concluida)
  def test_adia_notificacao(self):
    minutos_adiar = 35
    self.tarefa.data_notificacao = datetime(2022, 3, 19, 20, 15)
    dt_esperada = datetime(2022, 3, 19, 20, 15) + timedelta(minutes=minutos_adiar)
    self.tarefa.adiar_notificacao(minutos_adiar)
    self.assertEqual(self.tarefa.data_notificacao, dt_esperada)
  def test_descricao(self):
    descricao_nova = "Aula de Testes UnitTest"
    self.tarefa.adicionar_descricao(descricao_nova)
    self.assertEqual(self.tarefa.descricao, descricao_nova)
    pass
  def test_tarefa_atrasada(self):
    self.tarefa.data = datetime(2022, 4, 20, 10, 35)
    self.assertFalse(self.tarefa.atrasada())
    self.tarefa.data = datetime(2022, 1, 20, 10, 35)
    self.assertTrue(self.tarefa.atrasada())

unittest.main()
