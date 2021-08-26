# -*- coding: utf-8 -*-
"""
El CEO de una empresa de tecnología desea planificar las decisiones financieras que tomara en el siguiente año. La manera de planificarlas depende de lo siguiente:

Si actualmente su capital se encuentra con saldo negativo, pedirá un préstamo bancario para que su nuevo saldo sea de $10000 dólares.
Si su capital tiene actualmente un saldo positivo pedirá un préstamo bancario para tener un nuevo saldo de $20000 dólares,
pero si su capital tiene actualmente un saldo superior a los $20000 dólares no pedirá ningún préstamo.

 
Posteriormente repartirá su presupuesto de la siguiente manera:
$5000 dólares para equipo de cómputo
$2000 dólares para mobiliario
Y el resto la mitad será para la compra de insumos y la otra para otorgar incentivos al personal.

 
Desplegar que cantidades se destinaran para la compra de insumos e incentivos al personal y, en caso de que fuera necesario,
a cuánto ascendería la cantidad que se pediría al banco.
@author: marco
"""
equipoComputo=5000
mobiliario=2000
saldo=int(input("Ingrese su saldo actual: $"))


if(saldo<0):
    prestamo=10000-saldo
    saldo+=prestamo

elif(saldo>20000):
    prestamo=0
    
else:
    prestamo=20000-saldo
    saldo+=prestamo


saldo-=equipoComputo
saldo-=mobiliario
insumos=saldo*0.5
saldo-=insumos
incetivos=saldo
saldo-=incetivos

print(f"\n\nPRESTAMO BANCARIO= ${prestamo}")
print(f"\nPRESUPUESTO:\nCOMPRA DE INSUMOS: ${insumos},\nINCETIVOS AL PERSONAL: ${incetivos}")

