count = 1

nomes = []

while count < 4: 
    nome = input(f"Digite um nome {count}: ")
    nomes.append(nome)

    count +=1

nomes.sort()
print(nomes)