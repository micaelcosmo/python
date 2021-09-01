from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('~-' * 30)
    print(f'A contagem de {i} até {f} de {p} em {p}:')

    if i <= f:
        while i <= f:
            print(f'{i}', end=' ')
            i += p
            sleep(0.3)
    else:
        while i >= f:
            print(f'{i}', end=' ')
            i -= p
            sleep(0.3)
    print('Fim!')


contador(1, 10, 1)
contador(0, 10, 2)
print('~-' * 30)
print('Agora é a sua vez de personalizar a contagem.')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
