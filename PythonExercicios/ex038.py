numeroUm = int(input('Digite um número: '))
numeroDois = int(input('Digite outro número: '))

maiorUm = numeroUm > numeroDois
maiorDois = numeroDois > numeroUm

if maiorUm:
    print('O {}primeiro valor{} é {}maior{}.'.format('\033[32m', '\033[m', '\033[34m', '\033[m'))
elif maiorDois:
    print('O {}segundo valor{} é {}maior{}.'.format('\033[32m', '\033[m', '\033[34m', '\033[m'))
else:
    print('{}Não existe{} valor maior, os dois são {}iguais{}.'.format('\033[31m', '\033[m', '\033[33m', '\033[m'))