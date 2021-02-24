numero = int(input('Digite um número: '))
escolha = int(input('Escolha a base de conversão (1-> Binário, 2->Octal, 3->Hexadecimal): '))

binario = escolha == 1
octal = escolha == 2
hexadecimal = escolha == 3

if binario:
    resultado = format(bin(numero)[2:])
elif octal:
    resultado = format(oct(numero)[2:])
elif hexadecimal:
    resultado = format(hex(numero)[2:])

print(resultado)