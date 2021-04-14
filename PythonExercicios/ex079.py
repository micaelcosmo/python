numeros = []
continuar = ''
while True:
    numero = int(input('Digite um valor: '))
    if numero not in numeros:
        print('Valor adicionado com sucesso...')
        numeros.append(numero)
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N]: '))
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break
print('PROGRAMA ENCERRADO COM SUCESSO')
numeros.sort()
print(f'Os valores únicos digitados foram: {numeros}')
