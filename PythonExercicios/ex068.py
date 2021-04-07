import random
numero = numero_Computador = contador = total = 0
resultado = jogador = par_Impar = ''
while True:
    escolha_Jogador = str(input('Par ou Ímpar? ->[P/I]<- '))
    while escolha_Jogador not in 'PI':
        escolha_Jogador = str(input('Par ou Ímpar? ->[P/I]<- '))
    numero = int(input('Digite um valor: '))
    numero_Computador = random.randint(1, 10)
    total = numero + numero_Computador
    if total % 2 == 0:
        resultado = "P"
        par_Impar = 'Par'
        if resultado == escolha_Jogador:
            contador += 1
            print(f'Sua escolha foi {escolha_Jogador}')
            print(f'Você jogou {numero} e o computador {numero_Computador}. Total de {total} deu {par_Impar}.')
            print('Você GANHOU! Vamos jogar novamente...')
        elif resultado != escolha_Jogador:
            print(f'Sua escolha foi {escolha_Jogador}')
            print(f'Você jogou {numero} e o computador {numero_Computador}. Total de {total} deu {par_Impar}.')
            print('Você PERDEU!')
            break
    else:
        resultado = "I"
        par_Impar = 'Ímpar'
        if resultado == escolha_Jogador:
            contador += 1
            print(f'Sua escolha foi {escolha_Jogador}')
            print(f'Você jogou {numero} e o computador {numero_Computador}. Total de {total} deu {par_Impar}.')
            print('Você GANHOU! Vamos jogar novamente...')
        else:
            print(f'Sua escolha foi {escolha_Jogador}')
            print(f'Você jogou {numero} e o computador {numero_Computador}. Total de {total} deu {par_Impar}.')
            print('Você PERDEU!')
            break
print(f'GAME OVER!!! Total de vitórias: {contador}')
