# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:59:01 2021

@author: marco
"""
#

pob_barr=int(input("INGRESE LA POBLACION DE BARRANQUILLA: "))
pob_bog=int(input("INGRESE LA POBLACION DE BOGOTA: "))
año=0

while pob_barr<pob_bog:
    año+=1
    pob_barr+=(pob_barr*0.0235)
    pob_bog+=(pob_bog*0.0106)
    pob_barr=int(pob_barr)
    pob_bog=int(pob_bog)
print(f"AÑO {año}: \nPoblacion de Barranquilla: {pob_barr} \nPoblacion de Bogota: {pob_bog}\n\n")
    #Al multiplicar por decimales se pone personas incompletas