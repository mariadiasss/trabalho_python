def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicita um número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Chama a função e exibe o resultado
tabuada(numero)