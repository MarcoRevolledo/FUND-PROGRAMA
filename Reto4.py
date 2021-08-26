'''
Juan Pablo Montoya, entrena todos los días, recorriendo cierta cantidad de kilómetros, 
de tal forma que todos los días recorre el doble de lo que recorrió el día anterior más 10 km.
Pero cada 3 días recorre solo la mitad de lo que recorrió el día anterior.
Realice una función que dado el número de kilómetros recorridos el primer día del entrenamiento y un número
n de días y halle el total de kilómetros acumulados hasta ese día (el n-ésimo día).

'''
def kilometraje(kms_ini, nd):
    v=2
    acumulado=kms_ini
    cant_rec=kms_ini
    print(f"\nDIA:1 CANTIDAD A RECORRER: {cant_rec} ACUMULADO: {acumulado}")
    for i in range(nd-1):
        if(v==1 or v==2):
           cant_rec=(cant_rec*2)+10
           acumulado+=cant_rec
           
           print(f"DIA:{v} CANTIDAD A RECORRER: {cant_rec} ACUMULADO: {acumulado}")
           v+=1
        elif(v==3):
            cant_rec=cant_rec/2
            acumulado+=cant_rec
            print(f"DIA:{v} CANTIDAD A RECORRER: {cant_rec} ACUMULADO: {acumulado}")
            v=1
    
    print(f"\nEL ACUMULADO EN {nd} DIAS, ES: {acumulado} ")
    
    
while True:
    try:
        
        nd=int(input("DIGITE LA CANTIDAD DE DIAS QUE TRANSCURREN: "))
        break
    
    except(ValueError, TypeError)  :
        print("INGRESE UNA CANTIDAD ENTERA.\n")  
        

while True:
    try:
        
        kms=float(input("INGRESE LA CANTIDAD DE KILOMETROS INICIALES: "))
        break
        
    except(ValueError, TypeError, ZeroDivisionError)  :
        print("INGRESE UNA CANTIDAD CORRECTA.\n")  


kilometraje(kms, nd)