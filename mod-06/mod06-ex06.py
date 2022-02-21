lista = [1, 3, 2, 5]
...
# Deve imprimir 5

maior = None

for num in lista:
    if maior == None or num > maior:
        maior = num

print(maior)
