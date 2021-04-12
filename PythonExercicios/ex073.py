times = ('Flamengo Esports', 'VORAX', 'RED Kaluga', 'LOUD', 'PaiN Gaming', 'KaBuM! Esports', 'INTZ', 'Cruzeiro eSports',
         'FURIA', 'RENSGA')
print('Dados da classificação CBLOL 2021 (antes da final)')
print(f'Os 5 primeiros colocados são:\n {times[:5]}')
print(f'Os 4 últimos colocados são:\n {times[6:]}')
print(f'Times participantes por ordem alfabética:\n {sorted(times)}')
print(f'O time da KaBuM! está na {times.index("KaBuM! Esports")+1}ª posição.')
