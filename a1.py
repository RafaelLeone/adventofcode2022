with open("./a-dados") as f:
    dados = f.readlines()
mapa_da_soma_de_calorias_dos_elfos = {}
elfo = 0
calorias = 0

for comida in dados:
    if comida not in ['\n', '\r', '\r\n']:
        calorias += int(comida)
    else:
        mapa_da_soma_de_calorias_dos_elfos[elfo] = calorias
        elfo += 1
        calorias = 0

maior = max(mapa_da_soma_de_calorias_dos_elfos.values())

print(maior)
