import csv

def ler_csv_como_tabela():
    try:
        with open("dados.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print("\t".join(linha))
    except FileNotFoundError:
        print("Erro: o arquivo 'dados.csv' não foi encontrado.")

ler_csv_como_tabela()