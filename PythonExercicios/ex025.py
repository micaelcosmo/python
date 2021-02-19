nome = str(input('Digite seu nome completo: ')).lower()
sob = nome.rfind('cosmo')
if sob == -1:
    print('O seu nome não tem Cosmo.')
elif sob >= 0:
    print('O seu nome possui o Cosmo!')

'''
nome = str(input('Qual é o seu nome completo?')).strip()
print('Seu nome tem Cosmo? {}'.format('cosmo' in nome.lower()))
'''