while True:
    value_one = int(input("Digite o primeiro valor: "))
    value_two = int(input("Digite o segundo valor: "))
    value_three = int(input("Digite o terceiro valor"))

    if value_one > value_two and value_one > value_three:
        print(f"O maior valor é o: {value_one}")
    elif value_two > value_one and value_two > value_three:
        print(f"O maior valor é o: {value_two}")
    elif value_three > value_one and value_three > value_two:
        print(f"O maior valor é o: {value_three}")
    else:
        print("Os valores são equivalentes.")

    keep = input("Deseja continuar? (s/n)\n").lower()

    if keep == "n":
        print("Encerrando programa.")
        break