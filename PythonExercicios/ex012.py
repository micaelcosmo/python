p1 = float(input('Digite o preço do produto: R$'))
p2 = (p1/100) * 5
p3 = p1 - p2
#p2 = p1 - (p1 * 5 / 100)
print('O valor do produto com 5% de desconto é: R${:.2f}'.format(p3))