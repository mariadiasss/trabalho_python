def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vogais)

# Solicita uma frase ao usuário
frase = input("Digite uma frase para contar as vogais: ")

# Chama a função e exibe o resultado
resultado = contar_vogais(frase)
print(f"A quantidade de vogais na frase é: {resultado}")