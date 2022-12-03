with open("./c-dados") as f:
    dados = [l.strip('\n\r') for l in f]
compartimento1 = []
compartimento2 = []
contador = 0
soma = 0
# letras_que_ja_foram = []
#Dicionário de prioridade:
dict = {}
for char in range(26):
    c = char + 97
    dict[char+1] = chr(c)
for char in range(26):
    c = char + 65
    dict[char+27] = chr(c)
dict = {value:key for key, value in dict.items()}
#Dividindo compartimentos:
for mochila in dados:
    divisao = int(len(mochila)/2)
    compartimento1.append(mochila[:divisao])
    compartimento2.append(mochila[divisao:])

while contador < len(compartimento1):
    for letra in compartimento1[contador]:
        if letra in compartimento2[contador]:
            # and letra not in letras_que_ja_foram
            # letras_que_ja_foram.append(letra)
            soma += dict[letra]
            break
    contador += 1

print(soma)
