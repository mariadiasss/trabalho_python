def copiar_arquivo():
    try:
        with open("original.txt", "r") as original:
            conteudo = original.read()
        with open("copia.txt", "w") as copia:
            copia.write(conteudo)
    except FileNotFoundError:
        print("Erro: o arquivo 'original.txt' não foi encontrado.")

copiar_arquivo()