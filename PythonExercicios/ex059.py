primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))

print("Menu: \n - [1] SOMAR\n - [2] MULTIPLICAR\n - [3] MAIOR\n - [4] NOVOS NÚMEROS\n - [5] SAIR DO PROGRAMA")

QUANTIDADE_MENU = 5
SOMAR = 1
MULTIPLICADOR = 2
MAIOR = 3
NOVOS_NUMEROS = 4
SAIR_PROGRAMA = 5
r = 0

while r != QUANTIDADE_MENU:
    r = int(input("Digite a opção desejada: "))
    if r > QUANTIDADE_MENU:
        print("OPÇÃO INVÁLIDA!")
    elif r == SOMAR:
        print("A soma entre {} e {} é {}".format(primeiroNumero, segundoNumero, primeiroNumero + segundoNumero))
    elif r == MULTIPLICADOR:
        print("A multiplicação entre {} e {} é {}".format(primeiroNumero, segundoNumero, primeiroNumero * segundoNumero))
    elif r == MAIOR:
        if primeiroNumero > segundoNumero:
            print("{} é maior que {}.".format(primeiroNumero, segundoNumero))
        elif primeiroNumero == segundoNumero:
            print("Os número são iguais")
        else:
            print("{} é maior que {}.".format(segundoNumero, primeiroNumero))
    elif r == NOVOS_NUMEROS:
        primeiroNumero = float(input("Digite o primeiro número: "))
        segundoNumero = float(input("Digite o segundo número: "))
print("Programa encerrado.")
