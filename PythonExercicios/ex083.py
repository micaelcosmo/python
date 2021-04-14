expressao = str(input('Digite a expressão: '))
pilha_Checagem = list()
for simbolo in expressao:
    if simbolo == '(':
        pilha_Checagem.append('(')
    elif simbolo == ')':
        if len(pilha_Checagem) > 0:
            pilha_Checagem.pop()
        else:
            pilha_Checagem.append(')')
            break
if len(pilha_Checagem) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
