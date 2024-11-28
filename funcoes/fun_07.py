def calcular_preco_final(preco, desconto):
    return preco * (1 - desconto / 100)

# Solicita o preço e o desconto ao usuário
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

# Chama a função e exibe o resultado
preco_final = calcular_preco_final(preco, desconto)
print(f"O preço final do produto com desconto é: {preco_final:.2f}")