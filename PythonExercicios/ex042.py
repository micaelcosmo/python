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
escaleno = retaUm != retaDois and retaDois != retaTres and retaTres != retaUm

possibilidadeRetaUm = retaUm < doisTres and retaUm > difDoisTres
possibilidadeRetaDois = retaDois < umTres and retaDois > difUmTres
possibilidadeRetaTres = retaTres < umDois and retaTres > difUmDois

if possibilidadeRetaUm and possibilidadeRetaDois and possibilidadeRetaTres:
    if equilatero:
        resultado = 'Equilátero'
    elif isosceles:
        resultado = 'Isósceles'
    elif escaleno:
        resultado = 'Escaleno'
    print('É possível fazer um triângulo {} com essas retas.'.format(resultado))
else:
    print('Não é possível fazer um triângulo com essas retas.')
