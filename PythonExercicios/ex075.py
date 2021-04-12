um_Numero = int(input('Digite um número: '))
dois_Numero = int(input('Digite um número: '))
tres_Numero = int(input('Digite um número: '))
quatro_Numero = int(input('Digite um número: '))
em_Tupla = (um_Numero, dois_Numero, tres_Numero, quatro_Numero)
list = []
print(f'Você digitou os valores {em_Tupla}')
print(f'O valor 9 apareceu {em_Tupla.count(9)} vezes.')
if 3 in em_Tupla:
    print(f'O valor 3 apareceu na {em_Tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
for p in range(len(em_Tupla)):
    if em_Tupla[p] % 2 == 0:
        list.append(em_Tupla[p])
if len(list) == 0:
    print('Nenhum dos valores digitados é par.')
else:
    print(f'Valores pares digitados: {list}')
