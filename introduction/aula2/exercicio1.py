# 1 - Dada a entrada de um número -> Veficar se o número é positivo, negativo ou zero.

number = float(input("Digite um número: "))

if number > 0 :
    print("O número é positivo")
elif number == 0 :
    print("O número é igual a zero")
else:
    print("O número é negativo")