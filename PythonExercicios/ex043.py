peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))

imc = peso / (altura * altura)

print('O seu IMC é de {:.1f}'.format(imc))

abaixo = 18.5
ideal = 25
sobrepeso = 30
obesidade = 40

if imc <= abaixo:
    resultado = 'ABAIXO do peso normal.'
elif imc <= ideal:
    resultado = 'com o peso IDEAL.'
elif imc <= sobrepeso:
    resultado = 'um POUCO ACIMA do peso normal.'
elif imc <= obesidade:
    resultado = 'com OBESIDADE.'
else:
    resultado = 'com OBESIDADE MÓBIDA, cuidado!'

print('Você está {}'.format(resultado))