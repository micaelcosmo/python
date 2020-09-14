m = float(input('Digite uma metragem: '))
cm = m * 100
mm = m * 1000
if(m == 1):
    print('{} metro tem, {} centímetros e {} milímetros.'.format(m, cm, mm))
else:
    print('{} metros tem, {} centímetros e {} milímetros.'.format(m, cm, mm))