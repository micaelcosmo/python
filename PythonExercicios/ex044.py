valorProduto = float(input('Valor do produto(R$): '))
print('''FORMAS DE PAGAMENTO
     [ 1 ] à vista dinheiro/cheque
     [ 2 ] à vista cartão
     [ 3 ] 2x no cartão
     [ 4 ] 3x ou mais no cartão''')
formasPagamento = int(input('Qual é a opção? '))

DINHEIRO_CHEQUE = 1
CARTAO = 2
DUAS_VEZES = 3
TRES_MAIS = 4
descontoCinco = 0.05
descontoDez = 0.10
jurosVinte = 0.20
aVistaDinChe = valorProduto - (valorProduto * descontoDez)
aVistaCartao = valorProduto - (valorProduto * descontoCinco)
parcelaCartaoTres = valorProduto + (valorProduto * jurosVinte)

if formasPagamento == DINHEIRO_CHEQUE:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valorProduto, aVistaDinChe))
    print('Você teve 10% de desconto.')
elif formasPagamento == CARTAO:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valorProduto, aVistaCartao))
    print('Você teve 5% de desconto.')
elif formasPagamento == DUAS_VEZES:
    resultado = valorProduto / 2
    prEint('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(resultado))
    print('Sua compra vai custar R${:.2f} no final.'.format(valorProduto))
elif formasPagamento == TRES_MAIS:
    xParcela = int(input('Quantas parcelas? '))
    resultado = parcelaCartaoTres / xParcela
    print('Com 20% de juros.')
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(xParcela, resultado))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valorProduto, parcelaCartaoTres))
else:
    print('{}Código de pagamento inválido.{}'.format('\033[31m', '\033[m'))