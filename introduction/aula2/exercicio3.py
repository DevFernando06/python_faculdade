USER_NAME = "admin"
PASSWORD = "admin"

while True:
    user_name = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")

    if USER_NAME != user_name or PASSWORD != password:
        print("Senha incorreta")
        continue

    print("Bem-vindo, Admin")
    break
