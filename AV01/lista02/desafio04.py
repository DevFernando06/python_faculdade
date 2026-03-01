def validar_nome():
    while True:
        nome = input("Nome: ")
        if len(nome) > 3:
            return nome
        print("Erro: O nome deve ter mais que 3 caracteres.")


def validar_idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if 0 <= idade <= 150:
                return idade
            print("Erro: A idade deve estar entre 0 e 150.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")


def validar_salario():
    while True:
        try:
            salario = float(input("Salário: "))
            if salario > 0:
                return salario
            print("Erro: O salário deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")


def validar_sexo():
    while True:
        sexo = input("Sexo (f/m): ").lower()
        if sexo in ['f', 'm']:
            return sexo
        print("Erro: Digite 'f' ou 'm'.")


def validar_estado_civil():
    while True:
        estado = input("Estado Civil (s/c/v/d): ").lower()
        if estado in ['s', 'c', 'v', 'd']:
            return estado
        print("Erro: Digite 's', 'c', 'v' ou 'd'.")


nome = validar_nome()
idade = validar_idade()
salario = validar_salario()
sexo = validar_sexo()
estado_civil = validar_estado_civil()

print("\nDados cadastrados com sucesso!")
print(nome, idade, salario, sexo, estado_civil)