jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total_Partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total_Partidas):
    partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
jogador['gols por partida'] = partidas[:]
jogador['total de gols'] = sum(partidas)
print('-*' * 30)
print(jogador)
print('-*' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-*' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols por partida"])} partidas.')
for i, v in enumerate(jogador['gols por partida']):
    print(f'   ==> Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total de gols"]} gols.')
