with open("./c-dados") as f:
    dados = [l.strip('\n\r') for l in f]
compartimento1 = []
compartimento2 = []
contador = 0
soma = 0
#Dicionário de prioridade:
dict = {}
for char in range(26):
    c = char + 97
    dict[char+1] = chr(c)
for char in range(26):
    c = char + 65
    dict[char+27] = chr(c)
dict = {value:key for key, value in dict.items()}

while contador < len(dados)-2:
    for letra in dados[contador]:
        if letra in dados[contador+1] and letra in dados[contador+2]:
            soma += dict[letra]
            break
    contador += 3

print(soma)
