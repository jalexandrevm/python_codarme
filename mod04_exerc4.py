valor_compra = float(input("digite o valor da compra: "))
valor_frete = float(input("digite o valor do frete: "))
cliente_cadastrado = input("cadastrado no programa de fidelidade? (s/n) ")
print((valor_compra+valor_frete) > 100 or cliente_cadastrado.lower() == "s")
