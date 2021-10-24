from PythonExercicios.ex115.lib.interface import *
from PythonExercicios.ex115.lib.arquivo import *
from time import sleep

arq = 'Curso_de_Python.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida.\033[m')
    sleep(1)
