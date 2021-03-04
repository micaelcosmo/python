QUANTIDADE_PESSOAS = 5
maior = 0
menor = float('inf')

for p in range(0, QUANTIDADE_PESSOAS):
    pesos = (float(input("Digite o peso em quilograma(kg): ")))
    if pesos > maior:
        maior = pesos
    if pesos < menor:
        menor = pesos

print("O maior peso foi {}kg".format(maior))
print("O menor peso foi {}kg".format(menor))
