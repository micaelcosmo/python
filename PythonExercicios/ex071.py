import math

print('CAIXA ELETRÔNICO de PYTHON')
CEDULA_CINQUENTA = 50
CEDULA_VINTE = 20
CEDULA_DEZ = 10
CEDULA_UM = 1
quantidade_Cinquenta = quantidade_Vinte = quantidade_Dez = quantidade_Um = resto = 0
valor_Sacado = int(input('Qual valor quer sacar?(sem moedas)R$ '))
while True:
    if valor_Sacado > CEDULA_CINQUENTA:
        quantidade_Cinquenta = valor_Sacado / CEDULA_CINQUENTA
        resto = valor_Sacado % CEDULA_CINQUENTA
        if resto == 0:
            break
    if valor_Sacado > CEDULA_VINTE:
        if resto == 0:
            quantidade_Vinte = valor_Sacado / CEDULA_VINTE
            resto = valor_Sacado % CEDULA_VINTE
            if resto == 0:
                break
        elif resto > CEDULA_VINTE:
            quantidade_Vinte = resto / CEDULA_VINTE
            resto = resto % CEDULA_VINTE
            if resto == 0:
                break
    if valor_Sacado > CEDULA_DEZ:
        if resto == 0:
            quantidade_Dez = valor_Sacado / CEDULA_DEZ
            resto = valor_Sacado % CEDULA_DEZ
            if resto == 0:
                break
        elif resto > CEDULA_DEZ:
            quantidade_Dez = resto / CEDULA_DEZ
            resto = resto % CEDULA_DEZ
            if resto == 0:
                break
    if valor_Sacado >= CEDULA_UM:
        if resto == 0:
            quantidade_Um = valor_Sacado / CEDULA_UM
            resto = valor_Sacado % CEDULA_UM
            if resto == 0:
                break
        elif resto >= CEDULA_UM:
            quantidade_Um = resto / CEDULA_UM
            resto = resto % CEDULA_UM
            if resto == 0:
                break
    break
print(f'Total de {math.floor(quantidade_Cinquenta):.0f} cédulas de R$50,00')
print(f'Total de {math.floor(quantidade_Vinte):.0f} cédulas de R$20,00')
print(f'Total de {math.floor(quantidade_Dez):.0f} cédulas de R$10,00')
print(f'Total de {math.floor(quantidade_Um):.0f} cédulas de R$1,00')
