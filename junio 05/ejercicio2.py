'''
Crear una función que me permita leer una distancia en kilómetros y la
convierta a metros, centímetros y milímetros, se debe dar la opción al
usuario de solicitar en que unidad los necesita
'''

def convertidor(n,opcion):
    if(opcion=="mts"):
        return n*1000
    elif(opcion=="cms"):
        return n*100000
    elif(opcion=="mms"):
        return n*1000000

print("mts= COVERTIR KILOMETROS A METROS\ncms= COVERTIR KILOMETROS A CENTIMETROS\nmms= COVERTIR KILOMETROS A MILIMETROS") 
opcion=input("\nINGRESE EL COMANDO: ")
kilometros=float(input("INGRESE LA CANTIDAD DE KILOMETROS QUE DESEA CONVERTIR: "))
n=convertidor(kilometros,opcion)
print(f"\nKILOMETROS CONVERTIDOS ES IGUAL A: {n}{opcion}") 