from datetime import date

ano = int(input('Ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual - ano
idadeAlistar = 18
aindaVai = idade < idadeAlistar
passouHora = idade > idadeAlistar

print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoAtual))

if aindaVai:
    resultado = -1 * (idade - idadeAlistar)
    anoAlistar = anoAtual + resultado
    print('Ainda faltam {} anos para o alistamento.'.format(resultado))
    print('Seu alistamento será em {}.'.format(anoAlistar))
elif passouHora:
    resultado = -1 * (idadeAlistar - idade)
    anoAlistar = anoAtual - resultado
    print('Você já deveria ter se alistado há {} anos.'.format(resultado))
    print('Seu alistamento foi em {}.'.format(anoAlistar))
else:
    print('Você deve se alistar IMEDIATAMENTE.')