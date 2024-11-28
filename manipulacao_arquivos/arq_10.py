def adicionar_entrada_diario():
    try:
        with open("diario.txt", "a") as arquivo:
            entrada = input("Digite sua nova entrada no diário: ")
            arquivo.write(entrada + "\n")
    except FileNotFoundError:
        with open("diario.txt", "w") as arquivo:
            entrada = input("Digite sua primeira entrada no diário: ")
            arquivo.write(entrada + "\n")

adicionar_entrada_diario()