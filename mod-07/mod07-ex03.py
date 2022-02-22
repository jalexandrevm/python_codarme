def maior_idade(pessoa):
  nome, idade = pessoa
  if idade >= 18:
    print("maior de idade")
  else:
    print("menor de idade")


# função apenas para testar o código
def main():
  maior_idade(("Pedro", 19))
  maior_idade(("Jonas", 18))
  maior_idade(("Lúcia", 12))

main()
