numero = float(input("Digite um número: "))
fatorial = numero
fatorado = numero
while fatorial > 1:
    fatorial -= 1
    fatorado *= fatorial
print(fatorado)
