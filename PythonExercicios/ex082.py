numeros = []
pares = []
impares = []
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] '))
    elif continuar in 'Nn':
        break
print(f'A lista completa é {numeros}'
      f'\nA lista de pares é {pares}'
      f'\nA lista de ímpares é {impares}')
