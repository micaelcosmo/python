def leiaDinheiro(msg):
    """
    -> Valida se a mensagem é um preço válido.
    :param msg: Preço que se quer validar.
    :return: A validação se foi aceita ou não.
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if leiaFloat(entrada) == False:
            print(f'\033[0:31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaFloat(string):
    """
    -> Valida se a string pode ser float.
    :param string: string que deseja validar.
    :return: validação em Boolean.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False
