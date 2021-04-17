numeros = [[], []]
for n in range(0, 7):
    temporario = int(input(f'Digite o {n+1}º valor: '))
    if temporario % 2 == 0:
        numeros[0].append(temporario)
    else:
        numeros[1].append(temporario)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
