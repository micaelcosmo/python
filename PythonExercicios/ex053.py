from unidecode import unidecode
frase = str(input("Digite uma frase: "))
maiusculaEspaco = unidecode(frase.upper().replace(" ", ""))
resultado = frase + ": é um palíndromo."
for i in range(0, len(maiusculaEspaco)):
    if maiusculaEspaco[i] != (maiusculaEspaco[len(maiusculaEspaco) - i - 1]):
        resultado = frase + ": não é um palíndromo."
print(resultado)
