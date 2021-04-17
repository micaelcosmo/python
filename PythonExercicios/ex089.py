turma = list()
aluno = list()
nota = list()
resposta = ''
mostrar_Nota = 0
while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    nota.append(float(input('Digite a primeira nota: ')))
    nota.append(float(input('Digite a segunda nota: ')))
    aluno.append(nota[:])
    turma.append(aluno[:])
    aluno.clear()
    nota.clear()
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta not in 'SsNn':
        resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('No.', f'{"NOME":<10}', 'MÉDIA')
print('-' * 20)
for m in range(0, len(turma)):
    print(f'{m:<3} {turma[m][0]:<10} {(turma[m][1][0] + turma[m][1][1]) / 2}')
while True:
    mostrar_Nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar_Nota == 999:
        break
    else:
        print(f'As notas de {turma[mostrar_Nota][0]} são {turma[mostrar_Nota][1][0], turma[mostrar_Nota][1][1]}')
        print('-' * 20)
print('Finalizando...')
print('<' * 3, 'VOLTE SEMPRE', '>' * 3)
