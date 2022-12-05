with open("./e-dados") as f:
    dados = [l.strip('\n\r') for l in f]
linha = 0
numero_a_pular = 4
tabela = []
#Tabela de caixas:
while linha < len(dados):
    if dados[linha][1] == '1':
        numero_da_ultima_pilha = dados[linha][-2]
        break
    for index, letra in enumerate(dados[linha]):
        if letra == chr(32):
            print('ok', index, linha)
        if (index-1)%4 == 0:
            tabela.append(letra)
    linha += 1

print(tabela)