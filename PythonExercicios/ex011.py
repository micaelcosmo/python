la = float(input('Digite a largura da parede em metros: '))
al = float(input('Digite a altura da parede em metros: '))
ar = la * al
tin = ar / 2
print('A parede tem {:.1f}m², então é necessário {:.1f}litro(s) de tinta.'.format(ar, tin))