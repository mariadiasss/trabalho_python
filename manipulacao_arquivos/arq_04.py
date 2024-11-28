def somar_numeros():
    try:
        with open("numeros.txt", "r") as arquivo:
            numeros = arquivo.readlines()
            soma = sum(int(num.strip()) for num in numeros)
            print(f"A soma dos números é: {soma}")
    except FileNotFoundError:
        print("Erro: o arquivo 'numeros.txt' não foi encontrado.")

somar_numeros()