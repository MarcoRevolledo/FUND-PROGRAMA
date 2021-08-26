def op(a,b,o):
    if o == 1:
        return '={}'.format(a+b)
    elif o == 2:
        return '={}'.format(a-b)
    elif o == 3:
        return '={}'.format(a*b)
    elif o == 4:
        return '={}'.format(a/b)
    elif o == 6:
        exit()
print(op(int(input('Ingrese el primer numero: ')),
int(input('Ingrese el segundo numero: ')),
int(input('''Que operanción va a relizar?\n
1.suma\n2.resta\n3.multiplicacion\n4.division\n5.salir\n'''))))