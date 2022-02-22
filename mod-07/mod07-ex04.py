def maior_idade(pessoa):
  if type(pessoa) == tuple:
    nome, idade = pessoa
  elif type(pessoa) == dict:
    idade = pessoa["idade"]
  else: # desnecessário se argumento válido
    return "formato de pessoa inválido"
  if idade >= 18:
    print("maior de idade")
  else:
    print("menor de idade")

# função apenas para testar o código
def main():
  print("com tuplas")
  maior_idade(("Jonas", 18))
  maior_idade(("Lúcia", 12))
  print("com dicionários")
  maior_idade({"nome": "Vitor", "idade": 19})
  maior_idade({"nome": "Luana", "idade": 14})

# testando relação com tipos
def main_tipos():
  print(type(12) == int)
  print(type(("Pedro", 19)) == tuple)
  print(type({"nome": "Pedro", "idade": 19}) == dict)

main()
