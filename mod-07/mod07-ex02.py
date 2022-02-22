def posmaior(lista):
  maior = None
  pos = 0
  for i in range(len(lista)):
      if maior == None or lista[i] > maior:
          maior = lista[i]
          pos = i

  return (pos, maior)

# função apenas para testar o código
def main():

  tmp = [12, 3, 45, 23, 9, 17]

  print(posmaior(tmp))

main()
