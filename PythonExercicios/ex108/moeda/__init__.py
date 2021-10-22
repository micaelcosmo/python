def aumentar(preco, porcentagem):
    preco += preco / 100 * porcentagem
    return preco


def diminuir(preco, porcentagem):
    preco -= preco / 100 * porcentagem
    return preco


def dobro(preco):
    preco *= 2
    return preco


def metade(preco):
    preco /= 2
    return preco


def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

