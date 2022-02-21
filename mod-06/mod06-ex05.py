alunos = [
    {
        "nome": "Alice",
        "nota": 8,
    },
    {
        "nome": "Bob",
        "nota": 7,
    },
    {
        "nome": "Carlos",
        "nota": 9,
    }
]

soma = 0

for aluno in alunos:
  soma = soma + aluno["nota"]

print(soma // len(alunos))
