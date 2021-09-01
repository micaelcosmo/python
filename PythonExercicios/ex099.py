from time import sleep


def maior(* num):
    cont = maior = 0
    print('-.' * 30)
    print('Analizando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 3, 6, 4, 9, 5)
maior(4, 7, 0)
maior(2, 1)
maior(5)
maior()