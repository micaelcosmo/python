n = int(input('Digite um número inteiro: '))
cores = {'limpa':'\033[m',
        'vermelho':'\033[31m',
        'verde':'\033[32m'}
parImpar = n%2
if parImpar == 0:
    print('O número {}{}{} é Par.'.format(cores['vermelho'], n, cores['limpa']))
else:
    print('O número {}{}{} é ímpar.'.format(cores['verde'], n, cores['limpa']))