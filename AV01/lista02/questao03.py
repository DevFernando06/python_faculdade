while True :
    print("---------- Operacao Adicao ----------")
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite outro numero: "))

    print(n1 + n2)

    keep = input("Deseja continuar somando? [S | N]").upper()

    if keep == "N" :
        break
