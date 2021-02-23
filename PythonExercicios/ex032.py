ano = int(input('Digite o ano: '))
divisivel400 = ano % 400
divisivel4 = ano % 4
divisivel100 = ano % 100
if divisivel400 == 0:
    print('Esse ano é bissexto.')
else:
    if divisivel4 == 0 and divisivel100 != 0:
        print('Esse ano é bissexto.')
    else:
        print('Esse ano não é bissexto')