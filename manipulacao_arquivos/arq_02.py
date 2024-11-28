def ler_arquivo():
    try:
        with open("mensagem.txt", "r") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Erro: o arquivo 'mensagem.txt' não foi encontrado.")

ler_arquivo()