import random

r = random.randint(0, 10)
n = 0
c = 0
while n != r:
    n = int(input('Digite o número de 0 a 10 em que a máquina pensou: '))
    c += 1
if n == r:
    print('Você acertou o número. Mas precisou de {} tentativas.'.format(c))
