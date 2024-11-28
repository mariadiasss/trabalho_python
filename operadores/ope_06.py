def trocar_valores():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Troca de valores utilizando operadores matemáticos
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    
    print(f"Após a troca, o primeiro número é {num1} e o segundo número é {num2}")

trocar_valores()