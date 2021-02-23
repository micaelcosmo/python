distancia = int(input('Qual a distancia da viagem em Km? '))
kmPromocao = 200
taxaCurta = 0.50
taxaLonga = 0.45
if distancia <= kmPromocao:
    resultado = distancia*taxaCurta
else:
    resultado = distancia*taxaLonga
print('O valor da viagem de {}Km é de R${:.2f} reais.'.format(distancia,resultado))