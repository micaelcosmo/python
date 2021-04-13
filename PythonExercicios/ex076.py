produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 32)
print('{:^32}'.format('LISTAGEM DE PREÇO'))
print('-' * 32)
for x in range(0, len(produtos), 2):
    print(f'{produtos[x]:.<20} |RS {produtos[x + 1]:>7.2f}')
print('-' * 32)
