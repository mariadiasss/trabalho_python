produto = input("Qual é o nome do produto? ")
quantidade = int(input("Qual é a quantidade? "))
preco_unitario = float(input("Qual é o preço unitário? "))
valor_total = quantidade * preco_unitario
print(f"O valor total da compra de {quantidade} {produto}(s) é R${valor_total:.2f}.")