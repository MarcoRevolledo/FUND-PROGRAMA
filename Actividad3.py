# -*- coding: utf-8 -*-
"""
El centro medico Carlos Ardila Lule desea llevar el registro de las personas que
se han vacunado contra el COVID-19. Para tal fin el centro médico ha
determinado segmentar la jornada por edad; las personas que podrán recibir la
vacuna son los que se encuentren entre 50 y 60 años como grupo 1 y entre 61
en adelante como grupo 2.
El algoritmo deberá solicitarle a la persona encargada de hacer el registro el año
de nacimiento y así verificara que la persona está habilitada o no, si la persona
se encuentra habilitada se deberá suma al censo de vacunación. Al finalizar la
jornada el programa deberá mostrar un reporte de las personas vacunadas por
edad. El reporte se visualizará cuando se termine la jornada.

@author: marco


cg1=0
cg2=0
an=0
while an >= 0:
    an=int(input('Ingrese el año de nacimiento: '))
    if (2021-an) >= 50 and  (2021-an) <= 60:
        print('Está en el grupo 1 \n')
        cg1+=1
    elif (2021-an) >= 60:
        print('Está en el grupo 2 \n')
        cg2+=1
    else:
        print('No está priorizado')
    
total=cg1+cg2
pcg1=(cg1*100)/total
pcg2=(cg2*100)/total
print('El numerp de pacientes en grupo 1 es: ',cg1)
print('\nEl procetaje es: ',pcg1)
print('\nEl numero de pacientes en el grupo 2 es: ',cg2)
print('\nEl procetaje es: ',pcg2)

"""


"""
h=int(input('Ingrese la altura: '))
rebotes=0
f=h
while f>(h*0.1):
    rebotes+=1
    f-=(f*0.1)
print('rebotes: ', rebotes)

"""