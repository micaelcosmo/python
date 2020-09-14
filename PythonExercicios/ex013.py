s1 = float(input('Digite o salário atual do funcionário: R$'))
c = (s1/100) * 15
s2 = s1 + c
#c = s1 + (s1 * 15 / 100)
print('Salário com 15% de aumento fica: R${:.2f}'.format(s2))