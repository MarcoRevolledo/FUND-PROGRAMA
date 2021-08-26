'''
Autor: Marco Revolledo Jaramillo
Programa: Mision Tic 2022
Universidad: UNAB

Reto 1
 ¡Qué bueno! Acabas de recibir tu primer salario luego de una ardua jornada de trabajo.
 Piensas por unos instantes en lo que vas hacer con el dinero que has recibido. De manera
 casi inmediata, vienen a tu mente varias ideas; sin embargo, decides rápidamente la forma
 en la que distribuirás el dinero. Un 20 % para compra de alimentos, 15% para compra de pasajes,
 10% para compra de boletos de cine, 15% para compra de libros y el dinero restante debe ser
 destinado para el pago del alquiler del lugar donde estás viviendo. 
'''

#Solucion
print('')
print('Bienvenido Estimado trabajador')
print('Para obtener los totales de los valores para repartir su salario.')
salario=int(input('Ingrese su sueldo: $') )

#Procedimientos
alimentos=salario*0.2
pasajes=salario*0.15
cine=salario*0.1
libros=salario*0.15
arriendo=salario*0.4
total=alimentos+pasajes+cine+libros+arriendo

print('')
print('Debe distribuir el salario de la siguiente forma:')
print('Compra de Alimentos:       $', alimentos)
print('Compra de Pasajes:         $', pasajes)
print('Compra de Boletos de cine: $', cine)
print('Compra de Libros:          $', libros)
print('Pago del Alquiler:         $', arriendo)
print('_______________________________________________')
print('                      Total $', total)