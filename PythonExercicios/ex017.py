import math
#   from math import hypot
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
#   hi = (co ** 2 + ca ** 2) ** (1/2)
#   print('Em um triângulo retângulo de cateto oposto {:.2f} e cateto adjacente {:.2f} sua hipotenusa é {:.2f}.'.format(co,ca,hi))
print('Em um triângulo retângulo de cateto oposto {:.2f} e cateto adjacente {:.2f} sua hipotenusa é {:.2f}.'.format(co,ca,math.hypot(co,ca)))
