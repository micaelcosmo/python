retaUm = int(input('Valor da primeira reta: '))
retaDois = int(input('Valor da segunda reta: '))
retaTres = int(input('Valor da terceira reta: '))

umDois = retaUm+retaDois
umTres = retaUm+retaTres
doisTres = retaDois+retaTres

difUmDois = retaUm-retaDois
difUmTres = retaUm-retaTres
difDoisTres = retaDois-retaTres

possibilidadeRetaUm = retaUm < doisTres and retaUm > difDoisTres
possibilidadeRetaDois = retaDois < umTres and retaDois > difUmTres
possibilidadeRetaTres = retaTres < umDois and retaTres > difUmDois

if possibilidadeRetaUm and possibilidadeRetaDois and possibilidadeRetaTres:
    print('É possível fazer um triângulo com essas retas.')
else:
    print('Não é possível fazer um triângulo com essas retas.')


