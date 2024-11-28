inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

if inicio > fim:
    print("Erro: o início não pode ser maior que o fim.")
else:
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            print(i)