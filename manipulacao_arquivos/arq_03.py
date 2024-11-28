def gravar_usuario():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    with open("usuario.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome}, Idade: {idade}\n")

gravar_usuario()