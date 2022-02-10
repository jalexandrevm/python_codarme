valor_compras = 0.0
desconto = 0.0
quantidade_itens = 0
valor_compras = float(input("digite o valor total das compras: "))
desconto = float(input("digite o valor do desconto: "))
quantidade_itens = int(input("digite a quantidade de itens: "))
print("o valor final das compras é: "+str(valor_compras-desconto))
print("o custo médio ficou em: "+str((valor_compras-desconto)/quantidade_itens))
