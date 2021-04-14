numeros = []
maior = 0
menor = float('inf')
for numero in range(0, 5):
    numeros.append(int(input('Digite um valor numérico: ')))
    if numeros[numero] > maior:
        maior = numeros[numero]
    if numeros[numero] < menor:
        menor = numeros[numero]
print(f'Os valores digitados foram {numeros}')
print(f'O maior número foi {maior} e está na {numeros.index(maior)+1}ª posição.')
print(f'O menor número foi {menor} e está na {numeros.index(menor)+1}ª posição.')
