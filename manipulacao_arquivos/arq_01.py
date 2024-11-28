def criar_arquivo():
    with open("dados.txt", "w") as arquivo:
        arquivo.write("Este é o meu primeiro arquivo em Python!")

criar_arquivo()