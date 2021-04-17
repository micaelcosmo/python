from random import randint
from time import sleep
jogo_Unico = list()
jogos = list()
quantidade_Jogos = int(input(f'{"JOGO NA MEGA SENA":^30}\nQuantos jogos você quer sortear? '))
print('-' * 5, f'SORTEANDO {quantidade_Jogos} JOGOS ', '-' * 5)
for x in range(0, quantidade_Jogos):
    for y in range(0, 6):
        numero = randint(1, 60)
        while numero in jogo_Unico:
            numero = randint(1, 60)
        jogo_Unico.append(numero)
    jogo_Unico.sort()
    jogos.append(jogo_Unico[:])
    jogo_Unico.clear()
    sleep(1)
    print(jogos[x])
print('-' * 5, '< BOA  SORTE >', '-' * 5)
