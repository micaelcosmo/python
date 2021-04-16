dados_Temporarios = []
lista_Principal = []
maior = menor = 0
while True:
    dados_Temporarios.append(str(input('Nome: ')))
    dados_Temporarios.append(float(input('Peso: ')))
    if len(lista_Principal) == 0:
        maior = menor = dados_Temporarios[1]
    else:
        if dados_Temporarios[1] > maior:
            maior = dados_Temporarios[1]
        if dados_Temporarios[1] <menor:
            menor = dados_Temporarios[1]
    lista_Principal.append(dados_Temporarios[:])
    dados_Temporarios.clear()
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(f'Os dados foram {lista_Principal}')
print(f'Ao todo, você cadastrou {len(lista_Principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pesados in lista_Principal:
    if pesados[1] == maior:
        print(f'{pesados[0]}')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for leves in lista_Principal:
    if leves[1] == menor:
        print(f'{leves[0]}')
print()
