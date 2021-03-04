from datetime import date

IDADE_BASE = 18
SE_MAIOR = "Já atingiu a Maioridade."
SE_MENOR = "Ainda não atingiu a Maioridade."
anoAtual = date.today().year
anoBase = anoAtual - IDADE_BASE
datas = []
maioridade = ""
quantidade = []

for x in range(0, 7):
    datas.append(int(input("Digite o ano de nascimento: ")))
    for y in range(0, len(datas)):
        if datas[y] <= anoBase:
            maioridade = SE_MAIOR
        else:
            maioridade = SE_MENOR
    quantidade.append(maioridade)
    print(maioridade)

quantidadeMaioridade = quantidade.count(SE_MAIOR)
quantidadeMinoridade = quantidade.count(SE_MENOR)

print((":-" * 17) + ":")
print("{} atingiram a maioridade.".format(quantidadeMaioridade))
print("{} ainda não atingiram a maioridade.".format(quantidadeMinoridade))
print((":-" * 17) + ":")
