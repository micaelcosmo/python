from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 10),
        'jogador2': randint(1, 10),
        'jogador3': randint(1, 10),
        'jogador4': randint(1, 10)}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(jogo, '\n')
for i, v in enumerate(ranking):
    print(f'{i+1}º colocado foi {v[0]} que tirou {v[1]} no d10')
