def aumentar(valor, porcentagem):
    valor += valor / 100 * porcentagem
    return valor


def diminuir(valor, porcentagem):
    valor -= valor / 100 * porcentagem
    return valor


def dobro(valor):
    valor *= 2
    return valor


def metade(valor):
    valor /= 2
    return valor
