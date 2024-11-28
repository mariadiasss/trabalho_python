def criar_arquivo_com_texto():
    nome_arquivo = input("Digite o nome do arquivo: ")
    texto = input("Digite o texto que deseja gravar: ")
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(texto)

criar_arquivo_com_texto()