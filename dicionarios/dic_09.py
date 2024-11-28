disciplinas = {}
for _ in range(4):
    nome_disciplina = input("Digite o nome da disciplina: ")
    nota = float(input(f"Digite a nota de {nome_disciplina}: "))
    disciplinas[nome_disciplina] = nota
media = sum(disciplinas.values()) / len(disciplinas)
print(f"A média das notas é: {media:.2f}")