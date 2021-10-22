def leia_int(msg):
    """
    -> Analisa e valida a mensagem,
    aceitando apenas número Inteiro.
    :param msg: número que se quer validar.
    :return: número Inteiro válido.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leia_float(msg):
    """
    -> Analisa e valida a mensagem,
    aceitando apenas número Real.
    :param msg: número que se quer validar.
    :return: número Real válido.
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número Real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leia_int('Digite um Inteiro: ')
n2 = leia_float('Digite um Real: ')
print(f'O valor Inteiro digitado foi {n1} e o real foi {n2}.')
