questions_positive = 0
questions = [
    "Telefonou para a vítima?\n", 
    "Esteve no local do crime?\n", 
    "Mora perto da vítima?\n", 
    "Devia para a vítima?\n",
    "Já trabalhou com a vítima?\n"
    ]
print("Responda as perguntas abaixo: (s/n)\n")

for question in questions:
    res = input(question).lower()
    if res == "s":
        questions_positive += 1

match questions_positive:
    case 0 | 1 :
        print("O interrogado é classificado com Inocente")
    case 2:
        print("O interrogado é classificado com Suspeito")
    case 3 | 4:
        print("O interrogado é classificado com Cúmplice")
    case 5:
        print("O interrogado é classificado com Assassino")
    
