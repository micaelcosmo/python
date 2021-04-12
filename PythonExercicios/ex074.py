from random import randint
maior = 0
menor = float('inf')
tupla_Aleatoria = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f'Dentre os números: \n {tupla_Aleatoria}')
for x in range(0, len(tupla_Aleatoria)):
    if tupla_Aleatoria[x] > maior:
        maior = tupla_Aleatoria[x]
    if tupla_Aleatoria[x] < menor:
        menor = tupla_Aleatoria[x]
print(f'O maior número é : {maior} \nE o menor número é: {menor}')
