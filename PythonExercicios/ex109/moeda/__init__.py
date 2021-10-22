def aumentar(preco, porcentagem, formatado=False):
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

