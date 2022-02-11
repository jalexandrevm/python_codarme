operando1 = float(input("digite o primeiro número: "))
operando2 = float(input("digite o segundo número: "))
operador = input("qual a operação? (+ - * /) ")
resultado = 0
if operador == "/":
    if operando2 != 0:
        resultado = operando1/operando2
    else:
        print("Não é possível realizar divisão por zero!")
        quit(0)
elif operador == "*":
    resultado = operando1*operando2
elif operador == "-":
    resultado = operando1-operando2
elif operador == "+":
    resultado = operando1+operando2
else:
    quit(0)
print(resultado)
