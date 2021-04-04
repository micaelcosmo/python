numero = contador = somatorio = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    contador += 1
    somatorio += numero
print(f'A soma dos {contador} valores foi {somatorio}!')
