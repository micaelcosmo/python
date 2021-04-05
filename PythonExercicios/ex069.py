continuar = 'S'
contador_Pessoas = contador_Maioridade = contador_Masculino = contador_Mulher_Menoridade = idade = 0
while continuar in 'Ss':
    contador_Pessoas += 1
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade > 17:
        contador_Maioridade += 1
    sexo = str(input('Sexo: [M/F] '))
    if sexo in 'Mm':
        contador_Masculino += 1
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] '))
    if idade < 20 and sexo in 'Ff':
        contador_Mulher_Menoridade += 1
    continuar = str(input('Deseja continuar? [S/N] '))
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] '))
print(f'{contador_Pessoas} pessoas cadastradas no total.')
print(f'Total de pessoas com mais de 18 anos: {contador_Maioridade}')
print(f'Ao todo temos {contador_Masculino} homens cadastrados.')
print(f'E temos {contador_Mulher_Menoridade} mulheres com menos de 18 anos.')
