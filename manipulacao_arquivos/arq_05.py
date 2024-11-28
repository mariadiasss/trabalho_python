def contar_palavras():
    try:
        with open("texto.txt", "r") as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            print(f"O número total de palavras é: {len(palavras)}")
    except FileNotFoundError:
        print("Erro: o arquivo 'texto.txt' não foi encontrado.")

contar_palavras()