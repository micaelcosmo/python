base = 0
while True:
    base = int(input("Digite um número (Negativo para encerrar):"))
    if base < 0:
        break
    print("Na multiplicação:")
    for multiplicador in range(1, 11, 1):
        resultado = base * multiplicador
        print("{} x {} = {}".format(base, multiplicador, resultado))
    print("Na divisão:")
    for multiplicador in range(1, 11, 1):
        resultado = base / multiplicador
        print("{} / {} = {:.1f}".format(base, multiplicador, resultado))
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
