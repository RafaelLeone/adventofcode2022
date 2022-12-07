with open("./g-dados") as f:
    dados = [l.strip('\n\r') for l in f]

nivel = 0
lista = []
# dict nivelpasta x conteudo:
dict = {}
linha = -1

for dado in dados:
    linha += 1
    dado = dado.split(' ')
    if dado[0] == '$': # Comandos
        if dado[1] == 'cd':
            if dado[2] == '/':
                nivel = 0
                pasta_atual = dado[2]
            if dado[2] == '..':
                nivel -= 1
            else:
                nivel += 1
                pasta_atual = dado[2]
        if dado[1] == 'ls':
            linha_antiga = linha
            lista = []
            try:
                while dados[linha+1][0] != '$':
                    hhh = dados[linha+1].split(' ')
                    if hhh[0] == 'dir':
                        lista.append(str(nivel)+hhh[1])
                    else:
                        lista.append(hhh[0])
                    linha += 1
                else:
                    linha = linha_antiga
                    oi = str(nivel-1)+pasta_atual
                    dict[oi] = lista
                    continue
            except:
                break
print(dict)

#Agora pegar pastas que não tem pastas dentro e somar seu valor final.

novo_dict = {}
for pasta, lista in dict.items():
    soma = 0
    contador_de_errado = 0
    for arquivo in lista:
        try:
            soma += int(arquivo)
        except:
            contador_de_errado += 1
    if contador_de_errado == 0:
        novo_dict[pasta] = soma
for pasta, lista in dict.items():
    for arquivo in lista:
        if arquivo in novo_dict:
            print('oi')
print(novo_dict)
