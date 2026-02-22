vowels = "aeiou"

while True:
    letter = input("Digite uma letra: ").lower()

    if letter in vowels:
        print("A letra digitada é uma vogal")
    else:
        print("A letra digitada é uma consoante")

    keep = input("Deseja continuar? (s/n):\n ").lower()

    if keep == "n":
        print("Encerrando programa.")
        break

