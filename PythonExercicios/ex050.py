numeros = []
resultado = 0

for numero in range(0, 6, 1):
    numeros.append(int(input("Digite um número:")))
    if numeros[numero] % 2 == 0:
        resultado += numeros[numero]

print("A soma de todos os números pares é {}".format(resultado))
