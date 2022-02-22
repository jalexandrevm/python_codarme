def fatorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

# função apenas para testar o código
def main():
    print(fatorial(0))
    print(fatorial(5))
    print(fatorial(7))

main()
