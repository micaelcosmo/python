inicio = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
fim = inicio + (razao * 10)

for pa in range(inicio, fim, razao):
    print(pa)
