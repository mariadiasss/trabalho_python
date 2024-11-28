def é_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

# Solicita um ano ao usuário
ano = int(input("Digite um ano para verificar se é bissexto: "))

# Chama a função e exibe o resultado
if é_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")