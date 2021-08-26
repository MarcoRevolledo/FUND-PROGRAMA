def tarifaBasica(numero):
    if(numero==1):
        return 20000
    elif(numero==2):
        return 40000
    elif(numero==3):
        return 50000
    else:
        return "Usted ingreso un estrato fuera de rango"
    
def totalPagarAbonado(tarifa, impulsos):
    total=tarifa+(impulsos*100)
    return total

def totalPagar(totales):
    totalpagar=0
    for i in totales:
        totalpagar+=i
        
    return totalpagar

    
listatotales=[]
n_abonados=int(input("DIGITE LA CANTIDAD DE ABONADOS QUE DESEE LLENAR: "))
for i in range(n_abonados):
    nombre=input("\nDIGITE SU NOMBRE: ")
    while True:
        try:
            estrato=int(input("INGRESE EL ESTRATO : "))
            if(estrato==1 or estrato==2 or estrato==3):
                break
            else:
                estrato=1/0
        except (ValueError, TypeError,ZeroDivisionError):
            print("INGRESE UN VALOR CORRECTO\n")
        
    impulsos=int(input("DIGITE LA CANTIDAD DE IMPULSOS: "))
    total=totalPagarAbonado(tarifaBasica(estrato),impulsos)
    listatotales.append(total)
    print(f"Sr {nombre}\nUsted debe recibir un total de: ${total}")

        
totalpagar=totalPagar(listatotales)
print(f"\nEl valor total a pagar por todos los abonados es: ${totalpagar}")