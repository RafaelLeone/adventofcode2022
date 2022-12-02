dados = open("./b-dados")
pontuacao = 0
sistema = {
    'B X': 1, 'C Y': 6,'A Z': 8, 
    'A X': 3, 'B Y': 5, 'C Z': 7, 
    'C X': 2, 'A Y': 4, 'B Z': 9,
    'B X\n': 1, 'C Y\n': 6,'A Z\n': 8, 
    'A X\n': 3, 'B Y\n': 5, 'C Z\n': 7, 
    'C X\n': 2, 'A Y\n': 4, 'B Z\n': 9
    }

for rodada in dados:
    pontuacao += sistema[rodada]

print(pontuacao)
