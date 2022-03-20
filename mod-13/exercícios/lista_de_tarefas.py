class ListaDeTarefas:
  def __init__(self) -> None:
    self._tarefas = []
    self._quantidade_tarefas = 0
  def __len__(self):
    return self._quantidade_tarefas
    pass
  def adicionar_tarefa(self, tarefa):
    self._tarefas.append(tarefa)
    self._quantidade_tarefas += 1
    pass
  def get_tarefas(self, incluir_concluidas=False):
    if not incluir_concluidas:
      lista_resultado = []
      for task in self._tarefas:
        if task.concluida == incluir_concluidas:
          lista_resultado.append(task)
      return lista_resultado
    else:
      return self._tarefas
    pass

  def get_tarefas_atrasadas(self):
    lista_resultado = []
    for task in self._tarefas:
      if task.atrasada():
        lista_resultado.append(task)
    return lista_resultado
    pass

  def get_tarefas_para_hoje(self):
    lista_resultado = []
    for task in self._tarefas:
      if task.pra_hoje():
        lista_resultado.append(task)
    return lista_resultado
    pass
