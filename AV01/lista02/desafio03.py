numbers = []
while True :
    number = int(input("Adicione um número a lista: "))
    if not 0 <= number <= 1000 :
        print("[ERROR] Adicione apenas números entre 0 e 1000")
        continue

    numbers.append(number)

    if len(numbers) < 2:
        continue 

    keep = input("Deseja continuar adicionando valores? [s | n]\n").lower()

    if keep == "n" :
        print("O maior valor da lista é: ", max(numbers))
        print("O menor valor da lista é: ", min(numbers))
        print("A soma de todos os valores lista é: ", sum(numbers))     
        break