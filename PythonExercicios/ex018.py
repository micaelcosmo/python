from math import radians, sin, cos, tan
a = float(input('Digite um ângulo: '))
print('O ângulo de {}º tem o SENO de {:.2f}'.format(a, sin(radians(a))))
print('O ângulo de {}º tem o COSSENO de {:.2f}'.format(a, cos(radians(a))))
print('O ângulo de {}º tem o TANGENTE de {:.2f}'.format(a, tan(radians(a))))
