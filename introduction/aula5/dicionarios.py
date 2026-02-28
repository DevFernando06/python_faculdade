lista = [
	{
		"nome" : "Joao",
		"idade": "21"
	},
    {
		"nome" : "Maria",
		"idade": "18"
	}
]

for contato in lista:
    if contato["nome"] == "Joao":
        print("Joao existe")
