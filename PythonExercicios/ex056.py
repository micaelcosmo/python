QUANTIDADE_PESSOAS = 4
somaIdade = 0
idadeMaior = 0
maisVelho = ""
quantidadeMulheres = 0

for x in range(0, QUANTIDADE_PESSOAS):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo[M/F]: "))
    print("=-" * 10)
    somaIdade += idade
    if idade > idadeMaior:
        idadeMaior = idade
        maisVelho = nome
    if sexo == "F" and idade < 20:
        quantidadeMulheres += 1

media = somaIdade / QUANTIDADE_PESSOAS

print("A idade média do grupo é de {:.0f} anos.".format(media))
print("O mais velho do grupo se chama, {}.".format(maisVelho))
print("Temos ao todo temos {} mulhere(s) no grupo com menos de 20 anos.".format(quantidadeMulheres))
