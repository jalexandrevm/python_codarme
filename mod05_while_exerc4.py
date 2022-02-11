num_sorte = 7
perdeujogo = True
tentativa = 1
num_informado = 0
while tentativa <= 3 and perdeujogo:
    num_informado = int(input("tente acertar o número secreto: "))
    if num_sorte == num_informado:
        perdeujogo = False
    elif num_informado < num_sorte:
        print("menor")
    elif num_informado > num_sorte:
        print("maior")
    tentativa += 1
print("perdeu" if perdeujogo else "ganhou")
