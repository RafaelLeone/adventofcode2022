with open("./f-dados") as f:
    string = [l.strip('\n\r') for l in f]
    string = str(string[0])

for contador in range(len(string)-13):
    conjunto_de_quatorze_letras = string[contador:contador+14]
    lista = [letra for letra in conjunto_de_quatorze_letras]
    alvo = [lista.count(letra) for letra in lista]
    quatorze_uns = alvo.count(1)
    if quatorze_uns == 14:
        break
    contador += 1
# Tem +13 por ser a última posição e +1 por começar do zero pelo código.
print(contador+14)
