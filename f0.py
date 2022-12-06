with open("./f-dados") as f:
    string = [l.strip('\n\r') for l in f]
    string = str(string[0])

for contador in range(len(string)-3):
    conjunto_de_quatro_letras = string[contador] + string[contador+1] + string[contador+2] + string[contador+3]
    lista = [letra for letra in conjunto_de_quatro_letras]
    alvo = [lista.count(letra) for letra in lista]
    if alvo == [1, 1, 1, 1]:
        certo = conjunto_de_quatro_letras
        break
    contador += 1
#Tem +3 por ser a última posição e +1 por começar do zero pelo código.
print(contador+4)
