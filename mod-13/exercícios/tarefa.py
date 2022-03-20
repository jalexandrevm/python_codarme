from datetime import date, datetime, timedelta
class Tarefa:
    def __init__(self, titulo, descricao="", data=None, data_notificacao=None) -> None:
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.data_notificacao = data_notificacao
        self.concluida = False
    def concluir(self):
        self.concluida = True
        pass
    def adicionar_descricao(self, descricao):
        self.descricao = descricao
        pass
    def adiar_notificacao(self, minutos):
        if self.data_notificacao is None:
            return
        else:
            self.data_notificacao += timedelta(minutes=minutos)
        pass
    def atrasada(self) -> bool:
        if self.data is None:
            return False
        if isinstance(self.data, datetime):
            dt_tarefa = date(self.data)
        else:
            dt_tarefa = self.data
        if dt_tarefa < date.today():
            return True
        else:
            return False
        pass
    # criado para suprir necessidade
    def pra_hoje(self):
        if self.data is None:
            return False
        if isinstance(self.data, datetime):
            dt_tarefa = date(self.data)
        else:
            dt_tarefa = self.data
        if dt_tarefa == date.today():
            return True
        else:
            return False
        

