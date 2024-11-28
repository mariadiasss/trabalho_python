def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Solicita um número ao usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Chama a função e exibe o resultado
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")