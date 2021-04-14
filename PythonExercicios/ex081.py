numeros = list()
continuar = ''
while True:
    numeros.append(int(input('Digite um número: ')))
    numeros.sort(reverse=True)
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))
    else:
        if continuar in 'Nn':
            break
print(f'Você digitou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
