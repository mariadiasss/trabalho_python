dicionario = {"Ana": 25, "João": 30, "Maria": 22}
nome = input("Digite o nome a ser buscado: ")
if nome in dicionario:
    print(f"{nome} foi encontrado no dicionário.")
else:
    print(f"{nome} não foi encontrado no dicionário.")