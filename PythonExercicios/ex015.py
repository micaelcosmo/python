a = int(input('Quantos dias alugados? '))
p = float(input('Quantos km rodados? '))
#dia = a * 60
#km = p * 0.15
# pago = (dia + km)
pago1 = (a * 60) + (p * 0.15)
print('O valor total a pagar é de R${:.2f}.'.format(pago1))