def inverte_lista(lista):
    tmp = []
    for itm in lista:
        tmp.insert(0, itm)
    return tmp

lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)
print(lista_invertida)
# [{1}, 5, "a"]
