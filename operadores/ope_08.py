preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))
valor_desconto = (preco * desconto) / 100
preco_final = preco - valor_desconto
print(f"O valor do desconto é {valor_desconto} e o preço final é {preco_final}.")