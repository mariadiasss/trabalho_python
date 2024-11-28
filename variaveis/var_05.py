salario_bruto = float(input("Qual é o seu salário bruto? "))
desconto = float(input("Qual é o valor do desconto? "))
salario_liquido = salario_bruto - desconto
print(f"Seu salário líquido é R${salario_liquido:.2f}.")