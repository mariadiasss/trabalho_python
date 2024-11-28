def calcular_desconto():
    preco = float(input("Digite o preço do produto: "))
    desconto = float(input("Digite a porcentagem de desconto: "))
    
    valor_desconto = (preco * desconto) / 100
    preco_final = preco - valor_desconto
    
    print(f"Valor do desconto: {valor_desconto}")
    print(f"Preço final do produto: {preco_final}")

calcular_desconto()