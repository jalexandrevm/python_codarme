USUARIO = "admin"
SENHA = "741258"

nome_user = input("digite o nome de usuário: ")
senha_user = input("digite sua senha: ")

if nome_user.__eq__(USUARIO) and senha_user.__eq__(SENHA):
    print("Autenticação Bem Sucedida")
elif not nome_user.__eq__(USUARIO):
    print("nome de usuário não existe")
elif not senha_user.__eq__(SENHA):
    print("senha do usuário incorreta")
