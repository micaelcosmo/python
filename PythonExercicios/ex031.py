'''distancia = int(input('Qual a distancia da viagem em Km? '))
kmPromocao = 200
taxaCurta = 0.50
taxaLonga = 0.45
if distancia <= kmPromocao:
    taxa = taxaCurta
else:
    taxa = taxaLonga
resultado = distancia * taxa
print('O valor da viagem de {}Km é de R${:.2f} reais.'.format(distancia,resultado))'''

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a comprar uma viagem de {}Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será  de RS{:.2f} reais.'.format(preco))

