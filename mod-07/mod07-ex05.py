def constalista(lista, elemento):
    for item in lista:
        if item == elemento:
            return True
    return False

# função apenas para testar o código
def main():
    print(constalista([4, 9, 12, 45, 63], 34))
    print(constalista([4, 9, 12, 45, 63], 45))
    print(constalista([4, 9, 12, 45, 63], 63))

main()
