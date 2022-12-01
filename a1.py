with open("./a1-dados") as f:
    dados = f.readlines()
mapa_da_soma_de_calorias_dos_elfos = {}
elfo = 0
calorias = 0
maior = 0

for comida in dados:
    if comida not in ['\n', '\r', '\r\n']:
        calorias += int(comida)
    else:
        mapa_da_soma_de_calorias_dos_elfos[elfo] = calorias
        if mapa_da_soma_de_calorias_dos_elfos[elfo] > maior:
            maior = mapa_da_soma_de_calorias_dos_elfos[elfo]
        elfo += 1
        calorias = 0

print(maior)
