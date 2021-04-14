numeros = []
for q in range(0, 5):
    numero = int(input('Digite um valor: '))
    if q == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(numeros):
            if numero <= numeros[posicao]:
                numeros.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-.' * 30)
print(f'Os valores digitados em ordem foram{numeros}')