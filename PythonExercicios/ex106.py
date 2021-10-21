from time import sleep

cores = ('\033[m',  # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[1;107m',    # 6 - branco
    )


def ajuda(com):
    """
    -> Função para consultar o Intecative Help do Python.
    :param com: nome do comando.
    :return: docstring do comando.
    """
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    """
    -> Função para criar cabeçalhos e títulos.
    :param msg: Mensagem do título.
    :param cor: Cor de fundo (0-6)
    :return: Mensagem padronizada como título.
    """
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(0.5)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input("Função ou Biblioteca -> "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
