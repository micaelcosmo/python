nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
reprovado = media < 5.0
recuperacao = media >= 5.0 and media < 7.0
aprovado = media >= 7.0

print('Tirando {} e {}, a média do aluno é {}.'.format(nota1, nota2, media))

if reprovado:
    print('O aluno está {}REPROVADO{}.'.format('\033[31m', '\033[m'))
elif recuperacao:
    print('O aluno está de {}RECUPERAÇÃO{}.'.format('\033[33m', '\033[m'))
elif aprovado:
    print('O aluno está {}APROVADO{}.'.format('\033[32m', '\033[m'))