from PythonExercicios.ex115.lib.interface import *
from PythonExercicios.ex115.lib.arquivo import *
from time import sleep

arq = 'Curso de python'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        print()
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida.\033[m')
    sleep(2)
