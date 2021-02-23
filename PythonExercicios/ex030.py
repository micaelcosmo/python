n = int(input('Digite um número inteiro: '))
parImpar = n%2
if parImpar == 0:
    print('O número {} é Par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))