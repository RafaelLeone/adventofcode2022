with open("./g-dados") as f:
    dados = [l.strip('\n\r') for l in f]
nivel = 0
pastas = { '/': [], }
linha = -1
nivel_x_pastas = { 0: ['/',], }

for dado in dados:
    dado = dado.split(' ')
    if dado[0] == '$': # Comandos
        if dado[1] == 'cd':
            if dado[2] == '/':
                nivel = 0
            if dado[2] == '..':
                nivel -= 1
            else:
                nivel += 1
                nivel_x_pastas[nivel] = []

nivel_mais_baixo = list(nivel_x_pastas.keys())
nivel_mais_baixo = nivel_mais_baixo[-1]

for dado in dados:
    linha += 1
    dado = dado.split(' ')
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
                        nivel_x_pastas[nivel].append(x[1])
                    else:
                        linha += 1
                        continue
                linha = linha_antiga
            except:
                continue
    else:
        continue

print(nivel_mais_baixo)
print(nivel_x_pastas)
