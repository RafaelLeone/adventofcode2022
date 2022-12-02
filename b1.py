dados = open("./b-dados")
pontuacao = 0
sistema = {
    'B X': 1, 'C Y': 2,'A Z': 3, 
    'A X': 4, 'B Y': 5, 'C Z': 6, 
    'C X': 7, 'A Y': 8, 'B Z': 9,
    'B X\n': 1, 'C Y\n': 2,'A Z\n': 3, 
    'A X\n': 4, 'B Y\n': 5, 'C Z\n': 6, 
    'C X\n': 7, 'A Y\n': 8, 'B Z\n': 9
    }

for rodada in dados:
    pontuacao += sistema[rodada]
    
print(pontuacao)
