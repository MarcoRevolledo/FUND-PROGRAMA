# -*- coding: utf-8 -*-
"""
Created on Wed May 19 21:14:51 2021

@author: marco
"""

n=int(input("Ingrese cuantas personas estan en el puesto: "))
ran1=0
ran2=0
ran3=0

for i in range(n):
    edad=int(input(f"Ingrese la edad de la persona {i+1}:"))
       
    if edad<20:
        print("Usted no estan en ningun rango permitido") 
    elif edad>=20 and edad<=40:
        ran1=ran1+1
    elif edad>40 and edad<=60:
        ran2=ran2+1
    else:
        ran3=ran3+1

per_vac=ran1+ran2+ran3
por_ran1=(ran1/per_vac)*100
por_ran2=(ran2/per_vac)*100
por_ran3=(ran3/per_vac)*100

print(f"El {por_ran1}% esta entre los 20 y 40 años")
print(f"El {por_ran2}% esta entre los 40 y 60 años")
print(f"El {por_ran3}% es mayor de 60 años")