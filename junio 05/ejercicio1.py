'''
ejercicio 1

Crear una función “escribirTablaMultiplicar”, que reciba como
parámetro un número entero, y escriba la tabla de multiplicar de ese
número hasta el 10 (por ejemplo, para el 3 deberá llegar desde 3x0=0
hasta 3x10=30).
'''


def multiplicar(n):
    for i in range(11):
        print(f'{n}x{i}= {n*i}')


multiplicar(int(input("DIGITE UN NUMERO PARA OBTENER LA TABLA: ")))