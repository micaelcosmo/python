from datetime import date

anoNasc = int(input('Ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual - anoNasc
idadeMirim = 9
idadeInfantil = 14
idadeJunior = 19
idadeSenior = 25

if idade <= idadeMirim:
    resultado = 'MIRIM'
elif idade <= idadeInfantil:
    resultado = 'INFANTIL'
elif idade <= idadeJunior:
    resultado = 'JUNIOR'
elif idade <= idadeSenior:
    resultado = 'SÊNIOR'
else:
    resultado = 'MASTER'

print('O atleta tem {} anos.'.format(idade))
print('Classificação: {}'.format(resultado))