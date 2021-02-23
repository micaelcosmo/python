frase = str(input('Digite uma frase: ')).upper().lstrip()
#Quantas vezes aparece a letra "x" na frase.
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
#Em que posição apareceu a primeira letra "x".
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
#Em que posíção apareceu a última letra "x".
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))