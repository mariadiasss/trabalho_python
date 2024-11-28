def dividir_inteiros():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    quociente = num1 // num2
    resto = num1 % num2
    
    print(f"Quociente da divisão: {quociente}")
    print(f"Resto da divisão: {resto}")

dividir_inteiros()