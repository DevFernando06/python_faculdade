def calcular(opc, number_one, number_two):
    match opc:
        case 1:
            return number_one + number_two
        case 2:
            return number_one - number_two
        case 3:
            return number_one * number_two
        case 4:
            if number_two == 0:
               return "Não é possível dividir por zero"
            return number_one / number_two


while True :
    opc = int(input("---------Calculadora---------\n" \
    "1 - Adição\n" \
    "2- Subtração\n" \
    "3 - Multiplicação\n" \
    "4 - Divisão\n" \
    "5 - Sair\n"))

    number_one = int(input("Digite um número: "))
    number_two = int(input("Digite outro número: "))
    
    result = calcular(opc, number_one, number_two)
    print(result)

