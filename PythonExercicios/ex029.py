velocidade = int(input('A quantos Km/h você passou medidor? '))
velocidadeMaxima = 80
taxaMulta = 7.00
if velocidade > velocidadeMaxima:
    valorMulta = (velocidade - velocidadeMaxima) * taxaMulta
    print('Você foi multado em R${:.2f} reais.'.format(valorMulta))
else:
    print('Você não foi multado.')