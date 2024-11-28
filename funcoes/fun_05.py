def media(lista):
    return sum(lista) / len(lista)

# Solicita uma lista de números ao usuário
numeros = list(map(float, input("Digite uma lista de números separados por espaço: ").split()))

# Chama a função e exibe o resultado
resultado = media(numeros)
print(f"A média dos números é: {resultado}")