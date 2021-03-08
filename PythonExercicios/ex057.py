masculino = 'M'
feminino = 'F'
r = ''
while r != masculino and r != feminino:
    r = str(input('Qual sexo você escolhe? [M/F]')).upper()
    if r != masculino and r != feminino:
        print("Sexo inválido.")
if r == masculino:
    print("Você escolheu o sexo Masculino")
if r == feminino:
    print("Você escolheu o sexo Feminino")
