matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma_Terceira_Coluna = maior_Segunda_Linha = 0
tabela = ''
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        soma_Terceira_Coluna += matriz[linha][2]
        if matriz[1][coluna] > maior_Segunda_Linha:
            maior_Segunda_Linha = matriz[1][coluna]
        tabela += f'[{matriz[linha][coluna]:^5}]'
    tabela += '\n'
print(tabela)
print(f'A soma de todos os valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma_Terceira_Coluna}')
print(f'O maior valor da segunda coluna é {maior_Segunda_Linha}')
