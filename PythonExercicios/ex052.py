numero = int(input("Digite um número inteiro positivo maior que 1: "))

if numero <= 1:
    print("{} não é VÁLIDO.".format(numero))

else:
    resultado = "é primo"
    if numero == 2:
        print("{} {}".format(numero, resultado))

    else:
        for x in range(2, numero):
            if numero % x == 0:
                resultado = "não é primo"
                break
        print("{} {}".format(numero, resultado))
