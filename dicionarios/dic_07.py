produtos = {
    "Arroz": 5.50,
    "Feijão": 7.80,
    "Açúcar": 3.20,
    "Café": 10.90,
    "Leite": 4.50
}
nome_produto = input("Digite o nome do produto: ")
if nome_produto in produtos:
    print(f"O preço de {nome_produto} é R${produtos[nome_produto]:.2f}")
else:
    print(f"O produto {nome_produto} não foi encontrado.")