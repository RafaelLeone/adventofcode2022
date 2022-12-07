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
                    lista.append(dados[linha+1])
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
        teste = arquivo.split(' ')
        if teste[0] == 'dir':
            contador_de_errado += 1
            break
        else:
            soma += int(teste[0])
    if contador_de_errado == 0:
        novo_dict[pasta] = soma #trocar o zero pelo nome de cada pasta

print(novo_dict)
