from random import randint
from time import sleep

print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

PEDRA = 0
PAPEL = 1
TESOURA = 2
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = int(input('Qual é a sua jogada? '))
maquina = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('O computador jogou {}'.format(itens[maquina]))

if maquina == PEDRA:
    if jogador == PEDRA:
        print('O jogador jogou {}'.format(itens[jogador]))
        print('A jogada deu Empate')
    elif jogador == PAPEL:
        print('O jogador jogou {}'.format(itens[jogador]))
        print('O jogador Ganhou')
    elif jogador == TESOURA:
        print('O jogador jogou {}'.format(itens[jogador]))
        print('O jogador Perdeu')
    else:
        print('JOGADA INVÁLIDA')
elif maquina == PAPEL:
    if jogador == PEDRA:
        print('O jogador jogou {}'.format(itens[jogador]))
        print('O jogador Perdeu')
    elif jogador == PAPEL:
        print('O jogador jogou {}'.format(itens[jogador]))
        print('A jogada deu Empate')
    elif jogador == TESOURA:
        print('O jogador jogou {}'.format(itens[jogador]))
        print('O jogador Ganhou')
    else:
        print('JOGADA INVÁLIDA')
elif maquina == TESOURA:
    if jogador == PEDRA:
        print('O jogador jogou {}'.format(itens[jogador]))
        print('O jogador Ganhou')
    elif jogador == PAPEL:
        print('O jogador jogou {}'.format(itens[jogador]))
        print('O jogador Perdeu')
    elif jogador == TESOURA:
        print('O jogador jogou {}'.format(itens[jogador]))
        print('A jogada deu Empate')
    else:
        print('JOGADA INVÁLIDA')
