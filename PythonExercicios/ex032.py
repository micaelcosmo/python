from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year

divisivel400 = ano % 400
divisivel4 = ano % 4
divisivel100 = ano % 100

if divisivel400 == 0:
    print('Esse ano {} é bissexto.'.format(ano))
else:
    if divisivel4 == 0 and divisivel100 != 0:
        print('Esse ano {} é bissexto.'.format(ano))
    else:
        print('Esse ano {} não é bissexto'.format(ano))