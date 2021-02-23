import random

r = random.randint(0,5)
n = int(input('Digite um número de 0 a 5: '))
if n == r:
    print('Você acertou o número.')
else:
    print('Você errou, o número é {}.'.format(r))
