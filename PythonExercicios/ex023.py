def descobrir(idx):
    if idx == 0:
        return 'unidade'
    if idx == 1:
        return 'dezena'
    if idx == 2:
        return 'centena'
    if idx == 3:
        return 'milhar'
    return 'classe de unidade não identificada'
n = str(input('Digite um número: '))

for idx, val in enumerate(n):
    classe_de_unidade = descobrir(idx)
    valor_unitario = n[len(n)-idx-1]
    print(f'O valor da {classe_de_unidade} é {valor_unitario}.')

'''
num = int(input('Informe um número: ')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}.'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
'''
