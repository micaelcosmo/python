from time import sleep


def contador(i, f, p):
    if i <= f:
        if p <= 0:
            p = 1
        while i <= f:
            print(f'{i}', end=' ')
            i += p
            sleep(0.3)
    else:
        if p <= 0:
            p = 1
        while i >= f:
            print(f'{i}', end=' ')
            i -= p
            sleep(0.3)
    print('Fim!')
    print('~-' * 30)


print('A contagem de 1 até 10 de 1 em 1:')
contador(1, 10, 1)
print('A contagem de 10 até 0 de 2 em 2:')
contador(0, 10, 2)

print('Agora é a sua vez de personalizar a contagem.')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
