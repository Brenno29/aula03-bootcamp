texto = "hoje é a nossa segunda aula bootcamp."

palavras = texto.split()

print(palavras)

contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] = +1
    else:
        contagem_de_palavras[palavra] = 1