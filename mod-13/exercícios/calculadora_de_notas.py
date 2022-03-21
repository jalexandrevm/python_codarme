class Aluno:
    _nome = ""
    _nota = 0
    def __init__(self, nome, nota) -> None:
        self._nome = nome
        self._nota = nota
    def get_nota(self):
        return self._nota
    def get_nome(self):
        return self._nome
        pass
    pass

class Turma:
    _matriculados = []
    _media = 0
    def add_aluno(self, aluno):
        self._matriculados.append(aluno)
    def set_nota_aprovacao(self, nota):
        self._media = nota
    def get_nota_aprovacao(self):
        return self._media
    def get_alunos(self) -> list:
        return self._matriculados
    def get_qtd_alunos(self) -> int:
        return len(self._matriculados)
    pass

class CalculadoraDeNotas:
    def __init__(self, turma: Turma) -> None:
        self.turma = turma
        pass
    def get_media(self):
        qtd_alunos = len(self.matriculados)
        soma = 0
        for aluno in self.matriculados:
            soma += aluno.get_nota()
        return 0 if qtd_alunos == 0 else (soma / qtd_alunos)
    def get_maior_nota(self):
        aluno_nota_alta = None
        for aluno in self.turma.get_alunos():
            if not aluno_nota_alta:
                aluno_nota_alta = aluno
            if aluno_nota_alta.get_nota() < aluno.get_nota():
                aluno_nota_alta = aluno
        return aluno_nota_alta.get_nota()
        pass
    def get_menor_nota(self):
        aluno_nota_baixa = None
        for aluno in self.turma.get_alunos():
            if not aluno_nota_baixa:
                aluno_nota_baixa = aluno
            if aluno_nota_baixa.get_nota() > aluno.get_nota():
                aluno_nota_baixa = aluno
        return aluno_nota_baixa.get_nota()
        pass
    def get_aprovados(self):
        lista_resultado = []
        for aluno in self.turma.get_alunos():
            if aluno.get_nota() >= self.media:
                lista_resultado.append(aluno)
        return lista_resultado
        pass
    def get_reprovados(self):
        lista_resultado = []
        for aluno in self.turma.get_alunos():
            if aluno.get_nota() < self.media:
                lista_resultado.append(aluno)
        return lista_resultado
        pass
    def get_notas_alpha(self):
        lista_resultado = []
        for aluno in self.turma.get_alunos():
            lista_resultado.append(
                aluno.get_nome(),
                self.converte_nota(aluno.get_nota())
            )
        return lista_resultado
        pass
    def converte_nota(self, nota):
        if nota == 10:
            return "A+"
        elif 9 <= nota < 10:
            return "A"
        elif 7 <= nota < 9:
            return "B"
        elif 5 <= nota < 7:
            return "C"
        elif 3 <= nota < 5:
            return "D"
        elif 1 <= nota < 3:
            return "E"
        elif 0 <= nota < 1:
            return "F"
        pass
    pass

"""
CALCULADORA DE NOTAS
====================
1. Recebe uma turma, composta por uma lista de Alunos(nome, nota) e média para aprovar um aluno.
2. Calcula a média das notas da turma (get_media).
3. Qual a maior e menor nota (get_maior_nota, get_menor_nota).
4. Retorna alunos aprovados e reprovados (get_aprovados, get_reprovados).
5. Retorna lista de notas em representação de "letra".
    - nota == 10       =>    "A+"
    - 9 <= nota < 10   =>    "A"
    - 7 <= nota < 9    =>    "B"
    - 5 <= nota < 7    =>    "C"
    - 3 <= nota < 5    =>    "D"
    - 1 <= nota < 3    =>    "E"
    - 0 <= nota < 1    =>    "F
"""
