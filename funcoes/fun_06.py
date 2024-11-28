def inverter(texto):
    return texto[::-1]

# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra para inverter: ")

# Chama a função e exibe o resultado
resultado = inverter(palavra)
print(f"A palavra invertida é: {resultado}")