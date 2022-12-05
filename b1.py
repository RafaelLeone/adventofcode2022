with open("./b-dados") as f:
    dados = [l.strip('\n\r') for l in f]
pontuacao = 0
# Fórmula do sistema: pontuação pela forma escolhida + pontuação por derrota, empate ou vitória.
sistema = {
    'B X': 1+0, 'C Y': 3+3, 'A Z': 2+6, 
    'A X': 3+0, 'B Y': 2+3, 'C Z': 1+6, 
    'C X': 2+0, 'A Y': 1+3, 'B Z': 3+6,
    }

for rodada in dados:
    pontuacao += sistema[rodada]

print(pontuacao)
