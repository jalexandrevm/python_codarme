entrada = input("digite uma palavra: ")

dic_letras = {}

for letra in entrada:
    if dic_letras.get(letra) == None:
        dic_letras[letra] = 1
    else:
        dic_letras[letra] = dic_letras[letra] + 1

print(dic_letras)
