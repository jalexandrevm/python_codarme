alunos = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
]

soma = 0

for nome, nota in alunos:
  soma = soma + nota

print(soma // len(alunos))
