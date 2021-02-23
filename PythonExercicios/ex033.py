primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))
terceiroNumero = int(input('Digite o terceiro número: '))

if primeiroNumero > segundoNumero and primeiroNumero > terceiroNumero:
    resultadoMaior = primeiroNumero
elif segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
    resultadoMaior = segundoNumero
elif terceiroNumero > primeiroNumero and terceiroNumero > primeiroNumero:
    resultadoMaior = terceiroNumero

if primeiroNumero < segundoNumero and primeiroNumero < terceiroNumero:
    resultadoMenor = primeiroNumero
elif segundoNumero < primeiroNumero and segundoNumero < terceiroNumero:
    resultadoMenor = segundoNumero
elif terceiroNumero < primeiroNumero and terceiroNumero < segundoNumero:
    resultadoMenor = terceiroNumero

print('Dentre os números: {}, {} e {}.'.format(primeiroNumero,segundoNumero,terceiroNumero))
print('O maior número é {} e o menor número é {}.'.format(resultadoMaior,resultadoMenor))