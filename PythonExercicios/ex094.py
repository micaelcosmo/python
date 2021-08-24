galera = list()
pessoa = dict()
soma = media_Idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] not in 'MF':
            print('Erro! Por favor, responda apenas "M" para masculino ou "F" para feminino.')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    resposta = str(input('Quer continuar?[S/N] ')).upper()[0]
    if resposta not in 'SN':
        print('Erro! Por favor, responda apenas "S" para sim e "N" para não.')
    if resposta in 'N':
        break
media_Idade = soma / len(galera)
print('-*' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade é de {media_Idade:.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' -> {p["nome"]} ', end='')
print()
print(f'Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] > media_Idade:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}')
print('--*--ENCERRADO--*--')
