numero = int(input('Digite um número: '))
escolha = int(input('Escolha a base de conversão (1-> Binário, 2->Octal, 3->Hexadecimal): '))

binario = escolha == 1
octal = escolha == 2
hexadecimal = escolha == 3

if binario:
    resultado = format(int(bin(numero), 2), 'b')
elif octal:
    resultado = format(int(oct(numero), 8), 'o')
elif hexadecimal:
    resultado = format(int(hex(numero), 16), 'x')

print(resultado)