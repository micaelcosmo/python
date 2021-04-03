resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N].')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}.'.format(quantidade, media))
print('O maior número foi {} e o menor número foi {}.'.format(maior, menor))
