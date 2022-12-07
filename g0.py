with open("./g-dados") as f:
    dados = [l.strip('\n\r') for l in f]
nivel = 0
pastas = { '/': [], }
linha = -1
quais_pastas_tem_em_quais_niveis = { 0: ['/',] }

for dado in dados:
    dado = dado.split(' ')
    print(dado)
    if dado[0] == '$': # Comandos
        if dado[1] == 'cd':
            if dado[2] == '/':
                nivel = 0
            if dado[2] == '..':
                nivel -= 1
            else:
                nivel += 1
                quais_pastas_tem_em_quais_niveis[nivel] = []

for dado in dados:
    linha += 1
    dado = dado.split(' ')
    print(dado)
    if dado[0] == '$': # Comandos
        if dado[1] == 'cd':
            if dado[2] == '/':
                nivel = 0
            if dado[2] == '..':
                nivel -= 1
            else:
                nivel += 1
        if dado[1] == 'ls':
            linha_antiga = linha
            try:
                while dados[linha+1][0] != '$':
                    x = dados[linha+1].split(' ')
                    if x[0] == 'dir':
                        linha += 1
                        quais_pastas_tem_em_quais_niveis[nivel].append(x[1])
                    else:
                        linha += 1
                        continue
                linha = linha_antiga
            except:
                continue
    else:
        continue

print(quais_pastas_tem_em_quais_niveis)
