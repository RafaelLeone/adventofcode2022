with open("./d-dados") as f:
    dados = [l.strip('\n\r') for l in f]
soma = 0

for dado in dados:
    par_de_areas = dado.split(',')
    area1 = par_de_areas[0].split('-')
    area2 = par_de_areas[1].split('-')
    area1 = list(range(int(area1[0]), int(area1[1])+1))
    area2 = list(range(int(area2[0]), int(area2[1])+1))
    if area1[0] in area2 and area1[-1] in area2:
        soma += 1
    elif area2[0] in area1 and area2[-1] in area1:
        soma += 1

print(soma)
