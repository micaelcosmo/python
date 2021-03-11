numero = int(input("Digite quantos termos você quer mostrar: "))
primeiroTermo = 0
segundoTermo = 1

if numero >=3:
    print('Estes são os {} primeiros termos na Sequência Fibonacci:'.format(numero))
    print('{}, {}'.format(primeiroTermo, segundoTermo), end='')
    contadorTermos = 3

    while contadorTermos <= numero:
        proximoTermo = primeiroTermo + segundoTermo
        print(', {}'.format(proximoTermo), end='')
        contadorTermos += 1
        primeiroTermo = segundoTermo
        segundoTermo = proximoTermo

else:
    print('A sequência de Fibonacci começa com 0 e 1.')
