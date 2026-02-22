while True:
    value_one = int(input("Digite o primeiro valor: "))
    value_two = int(input("Digite o segundo valor: "))

    if value_one > value_two:
        print(f"O maior valor é o {value_one}")
    elif value_two > value_one:
        print(f"O maior valor é o {value_two}")
    else:
        print("Os valores são equivalentes.")

    keep = input("Deseja continuar? (s/n)\n").lower()

    if keep == "n":
        print("Encerrando programa.")
        break


