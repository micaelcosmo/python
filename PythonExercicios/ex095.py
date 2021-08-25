time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total_Partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, total_Partidas):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SsNn':
            break
        print('Erro! Responda apenas com S ou N.')
    if resp in 'Nn':
        break

print('-*' * 30)
print('Cod. ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Digite o código do jogador para ver detalhes(999 ENCERRA): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Código de jogado encontrado!')
    else:
        print(f' --  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} marcou {g} gols.')

print(' <<< VOLTE SEMPRE >>> ')
