def maior(num1, num2, num3):
    return max(num1, num2, num3)

# Solicita os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chama a função e exibe o resultado
resultado = maior(numero1, numero2, numero3)
print(f"O maior número é: {resultado}")