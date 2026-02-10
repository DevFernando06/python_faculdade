idade = int(input("Digite sua idade"))

if idade >= 16:
    print("Seu voto é opcional")
elif idade >= 18:
    print("Seu voto é obrigatório")
elif idade < 16: 
    print("Você não pode votar")
    
