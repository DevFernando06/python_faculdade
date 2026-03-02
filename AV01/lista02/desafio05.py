while True: 
    try :
        number = int(input("Digite um número inteiro positivo: "))
    except ValueError :
        print("ERRO: valor atribuido errado!")
        continue

    primo = True
    if number < 2 :
        primo = False
    else :
        for i in range(2, number) :
            if number % i == 0 : 
                primo = False
                break

    if primo:
        print("O número é primo!")
    else : 
        print("O número não é primo!")

    keep = input("Deseja continuar? [s | n]:\n").lower()

    if keep == "n" :
        break