# para resolver o problema de soma entre dois números
# podemos usar um loop while ou a fórmula direta
# soma = ( num1 + num2 ) * qtd_num / 2

# vamos primeiro usar a fórmula com 2 números diferentes

num1 = float(input("digite o número inicial: "))
num2 = float(input("digite o número final: "))
print((num1+num2)*(num2-num1+1)/2)

# agora vamos usar a fórmula com o 1 e um número fornecido

num1 = 1
num2 = float(input("digite o número final: "))
print((num1+num2)*(num2-num1+1)/2)

# agora vamos usar o loop while

soma = 0
num1 = 1
num2 = float(input("digite o número final: "))
while num1 <= num2:
    soma += num1
    num1 += 1
print(soma)
