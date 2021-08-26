# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:20:19 2021

@author: marco
"""

numero1=int(input("Digite el primer numero: "))
numero2=int(input("Digite el segundo numero: "))
numero3=int(input("Digite el tercero numero: "))

if numero1<numero2 and numero1<numero3:
    if numero2<numero3:
      print("(",numero1,", ",numero2,",",numero3,")")
    else:
      print("(",numero1,", ",numero3,",",numero2,")")
            
elif  numero2<numero1 and numero2<numero3:
    if numero1<numero3:
        print("(",numero2,", ",numero1,",",numero3,")")
    else:
        print("(",numero2,", ",numero3,",",numero1,")")      
            
elif  numero3<numero1 and numero3<numero2:
    if numero1<numero2:
        print("(",numero3,", ",numero1,",",numero2,")")
    else:
        print("(",numero3,", ",numero2,",",numero1,")")