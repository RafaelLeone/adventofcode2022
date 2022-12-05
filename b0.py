with open("./b-dados") as f:
    dados = [l.strip('\n\r') for l in f]
pontuacao = 0
# Fórmula do sistema: pontuação pela forma escolhida + pontuação por derrota, empate ou vitória.
sistema = {
    'B X': 1+0, 'C Y': 2+0, 'A Z': 3+0, 
    'A X': 1+3, 'B Y': 2+3, 'C Z': 3+3, 
    'C X': 1+6, 'A Y': 2+6, 'B Z': 3+6,
    }

for rodada in dados:
    pontuacao += sistema[rodada]
    
print(pontuacao)
