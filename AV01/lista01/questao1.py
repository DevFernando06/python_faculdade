while True: 
    value = int(input("Digite um número inteiro: "))

    if value % 2 == 0:
        print("O número digitado é par")
    else:
        print("O valor digitado é impar")

    keep = input("Deseja continuar? (s/n): ").lower()

    if keep == "n":
        print("Programa encerrado.")
        break

    