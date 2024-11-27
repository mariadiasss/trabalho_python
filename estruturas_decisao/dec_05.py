numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    print(f"O resultado é: {numero1 + numero2}")
elif operador == "-":
    print(f"O resultado é: {numero1 - numero2}")
elif operador == "*":
    print(f"O resultado é: {numero1 * numero2}")
elif operador == "/":
    if numero2 != 0:
        print(f"O resultado é: {numero1 / numero2}")
    else:
        print("Erro: Divisão por zero.")
else:
    print("Erro: Operador inválido.")
