base = int(input("Digite um número: "))
print("Na multiplicação:")
for multiplicador in range(1, 11, 1):
    resultado = base * multiplicador
    print("{} x {} = {}".format(base, multiplicador, resultado))

print("Na divisão:")
for multiplicador in range(1, 11, 1):
    resultado = base / multiplicador
    print("{} / {} = {:.1f}".format(base, multiplicador, resultado))
