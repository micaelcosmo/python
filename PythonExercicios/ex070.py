continuar = 'S'
nome_Produto = ''
produto_Barato = ''
preco_Produto = total_Compra = acima_Mil = menor_Preco= 0
while continuar in 'Ss':
    nome_Produto = str(input('Nome do produto: '))
    preco_Produto = int(input('Valor do produto: '))
    if menor_Preco == 0:
        menor_Preco = preco_Produto
        produto_Barato = nome_Produto
    if preco_Produto < menor_Preco:
        menor_Preco = preco_Produto
        produto_Barato = nome_Produto
    total_Compra += preco_Produto
    if preco_Produto >= 1000:
        acima_Mil += 1
    continuar = str(input('Deseja continuar? [S/N] '))
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] '))
print(f'O valor total da compra é: R${total_Compra:.2f}.')
print(f'{acima_Mil} produtos custam mais de R$1000,00.')
print(f'O produto mais barato foi {produto_Barato} que custa R${menor_Preco:.2f}.')
