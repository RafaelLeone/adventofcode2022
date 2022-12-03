with open("./c-dados") as f:
    dados = [l.strip('\n\r') for l in f]
#Dicionário de prioridade:
dict = {}
for char in range(26):
    c = char + 97
    dict[char+1] = chr(c)
for char in range(26):
    c = char + 65
    dict[char+27] = chr(c)
#Dividindo compartimentos:
for mochila in dados:
    divisao = int(len(mochila)/2)
    compartimento1 = mochila[:divisao]
    compartimento2 = mochila[divisao:]

print(divisao, compartimento1, compartimento2)
