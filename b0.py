with open("./b-dados") as f:
    dados = f.readlines()
pontuacao = 0
# Fórmula do sistema: pontuação pela forma escolhida + pontuação por derrota, empate ou vitória.
sistema = {
    'B X': 1+0, 'C Y': 2+0, 'A Z': 3+0, 
    'A X': 1+3, 'B Y': 2+3, 'C Z': 3+3, 
    'C X': 1+6, 'A Y': 2+6, 'B Z': 3+6,
    'B X\n': 1+0, 'C Y\n': 2+0, 'A Z\n': 3+0, 
    'A X\n': 1+3, 'B Y\n': 2+3, 'C Z\n': 3+3, 
    'C X\n': 1+6, 'A Y\n': 2+6, 'B Z\n': 3+6
    }

for rodada in dados:
    pontuacao += sistema[rodada]
    
print(pontuacao)
