valorCasa = int(input('Qual o valor do imóvel? '))
valorSalario = int(input('Qual valor do seu salário? '))
pagamentoAnos = int(input('Em quantos anos pretende pagar? '))

prestacao = valorCasa / (pagamentoAnos * 12)
valorMaximo = valorSalario * 0.30
maximaAnos = 30

if prestacao <= valorMaximo and pagamentoAnos <= maximaAnos:
    print('{}Parabéns! Seu empréstimo está aprovado.{}'.format('\033[42m', '\033[m'))
    print('O valor da prestação é de {}R${:.2f}{} reais.'.format('\033[34m', prestacao, '\033[m'))
else:
    print('Seu empréstimo foi {}negado{}!'.format('\033[1;41m', '\033[m'))