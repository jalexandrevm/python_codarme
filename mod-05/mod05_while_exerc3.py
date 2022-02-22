numprimo = int(input("digite um número inteiro: "))

divisor = 2
primo = True

while divisor < numprimo and primo:
    if (numprimo % divisor == 0):
        primo = False
    divisor += 1

print("primo" if primo else "não primo")
