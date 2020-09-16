import random
aluno1: str = input('Digite o nome do primero aluno: ')
aluno2: str = input('Digite o nome do segundo aluno: ')
aluno3: str = input('Digite o nome do terceiro aluno: ')
aluno4: str = input('Digite o nome do quarto aluno: ')
alunoSorteado = str
indice = random.randint(1,4)
if(indice == 1):
    alunoSorteado = aluno1
elif(indice == 2):
    alunoSorteado = aluno2
elif(indice == 3):
    alunoSorteado = aluno3
elif(indice == 4):
    alunoSorteado = aluno4

print('O aluno sorteado para limpar o quadro é, {}!'.format(alunoSorteado))

# from random import choice
# n1 = str(input('Primeiro aluno: '))
# n2 = str(input('Segundo aluno: '))
# n3 = str(input('Terceiro aluno: '))
# n4 = str(input('Quarto aluno: '))
# lista = [n1, n2, n3, n4]
# escolhido = random.choice(lista)
# print('O aluno escohido foi {}'.format(escolhido))