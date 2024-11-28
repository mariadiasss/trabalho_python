livro = {
    "titulo": input("Digite o título do livro: "),
    "autor": input("Digite o autor do livro: "),
    "ano_publicacao": int(input("Digite o ano de publicação: "))
}
print("Dicionário do livro antes da atualização:", livro)
livro["ano_publicacao"] = int(input("Digite o novo ano de publicação: "))
print("Dicionário do livro atualizado:", livro)