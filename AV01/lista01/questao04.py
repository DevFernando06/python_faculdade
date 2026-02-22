grade_one = float(input("Digite a primeira nota: "))
grade_two = float(input("Digite a segunda nota: "))

average = (grade_one + grade_two) / 2

print(f"Média: {average:.2f}")

if average == 10:
    print("Aprovado com Distinção")
elif average >= 7:
    print("Aprovado")
else:
    print("Reprovado")