def aumentar(preco, porcentagem, formatado=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar.
    :param porcentagem: qual é a taxa do aumento.
    :param formatado: saída formatada ou não.
    :return: o valor reajustado, com ou sem formato.
    """
    preco += preco / 100 * porcentagem
    return preco if formatado == False else moeda(preco)


def diminuir(preco, porcentagem, formatado=False):
    preco -= preco / 100 * porcentagem
    return preco if formatado == False else moeda(preco)


def dobro(preco, formatado=False):
    preco *= 2
    return preco if formatado == False else moeda(preco)


def metade(preco, formatado=False):
    preco /= 2
    return preco if formatado == False else moeda(preco)


def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco = 0, taxaA = 10, taxaR = 5):
    """
    -> Formata a saída de um determinado preço,
    levando em conta as taxas de aumento ou
    redução.
    :param preco: preço original, sem formatação.
    :param taxaA: porcentagem de aumento.
    :param taxaR: porcentagem de redução.
    :return: Resumo da análise do valor já formatado.
    """
    print('.~' * 14)
    print('\t  RESUMO DO VALOR'.center(14))
    print('.~' * 14)
    print(f'Preço analizado: \t{moeda(preco)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'{taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}')
    print(f'{taxaR:2.0f}% de redução: \t{diminuir(preco, taxaR, True)}')
    print('.~' * 14)
