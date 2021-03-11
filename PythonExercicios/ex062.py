inicio = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 0
novoContador = 0
while contador < 10:
    contador += 1
    print(inicio)
    inicio += razao
    while contador >= 10:
        novoContador = int(input("Digite quantos termos a mais deseja ver (Digite 0 para finalizar o programa): "))
        fim = inicio + (razao * novoContador)
        contador += novoContador
        for pa in range(inicio, fim, razao):
            if novoContador > 0:
                print(pa)
                inicio += razao
        if novoContador == 0:
            print("Progressão finalizada com {} termos mostrados.".format(contador))
            break
