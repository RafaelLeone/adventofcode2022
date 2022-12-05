import re

with open("./e-dados") as f:
    dados = [l.strip('\n\r') for l in f]
linha = 0
numero_a_pular = 4
tabela = []
matriz = []
contador = 0
#Matriz de caixas:
while linha < len(dados):
    if dados[linha][1] == '1':
        numero_da_ultima_pilha = int(dados[linha][-2])
        break
    for index, letra in enumerate(dados[linha]):
        if (index-1)%4 == 0:
            tabela.append(letra)
    linha += 1
linha = 0
while linha < numero_da_ultima_pilha:
    matriz.append([])
    while contador < len(tabela):
        if tabela[contador] != ' ':
            matriz[linha].append(tabela[contador])
        contador += numero_da_ultima_pilha
    linha += 1
    contador = numero_da_ultima_pilha - (numero_da_ultima_pilha - linha)
#Listas de movimentos:
linha +=1
lista_de_movimentos = []
while linha < len(dados):
    lista_de_movimentos.append([])
    lista_de_movimentos[linha-10] = [int(s) for s in re.findall(r'\d+', dados[linha])]
    linha += 1
#Solução:
for comandos in lista_de_movimentos:
    matriz[comandos[2]-1].reverse()
    algumacoisa = matriz[comandos[1]-1][0:comandos[0]]
    algumacoisa.reverse()
    matriz[comandos[2]-1] += algumacoisa
    matriz[comandos[2]-1].reverse()
    for i in range(comandos[0]):
        matriz[comandos[1]-1].pop(0)

for lista in matriz:
    print(lista[0], end='')
