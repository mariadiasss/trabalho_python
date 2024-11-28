peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print("Peso normal.")
else:
    print("Acima do peso.")