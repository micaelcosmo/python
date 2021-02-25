retaUm = float(input('Valor da primeira reta: '))
retaDois = float(input('Valor da segunda reta: '))
retaTres = float(input('Valor da terceira reta: '))

umDois = retaUm+retaDois
umTres = retaUm+retaTres
doisTres = retaDois+retaTres

difUmDois = retaUm-retaDois
difUmTres = retaUm-retaTres
difDoisTres = retaDois-retaTres

equilatero = retaUm == retaDois == retaTres
isosceles = retaUm == retaDois != retaTres or retaDois == retaTres != retaUm or retaTres == retaUm != retaDois

possibilidadeRetaUm = doisTres > retaUm > difDoisTres
possibilidadeRetaDois = umTres > retaDois > difUmTres
possibilidadeRetaTres = umDois > retaTres > difUmDois

if possibilidadeRetaUm and possibilidadeRetaDois and possibilidadeRetaTres:
    if equilatero:
        resultado = 'Equilátero'
    elif isosceles:
        resultado = 'Isósceles'
    else:
        resultado = 'Escaleno'
    print('É possível fazer um triângulo {} com essas retas.'.format(resultado))
else:
    print('Não é possível fazer um triângulo com essas retas.')
