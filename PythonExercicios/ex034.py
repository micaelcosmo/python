salarioAtual = int(input('Digite seu salário atual: R$ '))
salarioPiso = 1250
aumentoSuperior = 0.10
aumentoInferior = 0.15

if salarioAtual > salarioPiso:
    aumento = aumentoSuperior
else:
    aumento = aumentoInferior
resultado = salarioAtual+(salarioAtual*aumento)
print('Seu salário atual com aumento é R${:.2f} reais.'.format(resultado))