numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 == numero2 == numero3:
    print("Os três números são iguais.")
else:
    maior = max(numero1, numero2, numero3)
    print(f"O maior número é {maior}.")