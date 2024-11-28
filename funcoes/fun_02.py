def é_par(numero):
    return numero % 2 == 0

# Solicita um número ao usuário
numero = int(input("Digite um número para verificar se é par: "))

# Chama a função e exibe o resultado
if é_par(numero):
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")