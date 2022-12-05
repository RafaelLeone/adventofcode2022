with open("./e-dados") as f:
    dados = [l.strip('\n\r') for l in f]
linha = 0
numero_a_pular = 4
tabela = []
matriz = []
contador = 0
numero_atual = 0
#Matriz de caixas:
while linha < len(dados):
    if dados[linha][1] == '1':
        numero_da_ultima_pilha = int(dados[linha][-2])
        break
    for index, letra in enumerate(dados[linha]):
        if (index-1)%4 == 0:
            tabela.append(letra)
    linha += 1
while numero_atual < numero_da_ultima_pilha:
    matriz.append([])
    while contador < len(tabela):
        if tabela[contador] != ' ':
            matriz[numero_atual].append(tabela[contador])
        contador += numero_da_ultima_pilha
    matriz[numero_atual].reverse()
    numero_atual += 1
    contador = numero_da_ultima_pilha - (numero_da_ultima_pilha - numero_atual)

print(matriz)
