from datetime import date

QUANTIDADE_PESSOAS = 7
IDADE_BASE = 18
anoAtual = date.today().year
anoBase = anoAtual - IDADE_BASE
quantidadeMaioridade = 0

for x in range(0, QUANTIDADE_PESSOAS):
    data = int(input("Digite o ano de nascimento: "))
    if data <= anoBase:
        quantidadeMaioridade += 1

quantidadeMinoridade = QUANTIDADE_PESSOAS - quantidadeMaioridade

print((":-" * 17) + ":")
print("{} atingiram a maioridade.".format(quantidadeMaioridade))
print("{} ainda não atingiram a maioridade.".format(quantidadeMinoridade))
print((":-" * 17) + ":")
