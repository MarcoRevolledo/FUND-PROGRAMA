
def calcularBandeja(huevos):
    huevosA=0
    huevosAA=0
    huevosAAA=0
    huevosBC=0
    bandejasA=0
    bandejasAA=0
    bandejasAAA=0
    bandejasBC=0
    
    for i in huevos:
        if i=="A":
            huevosA+=1
        elif i=="AA":
            huevosAA+=1
        elif i=="AAA":
            huevosAAA+=1
        elif i=="BC":
            huevosBC+=1

    bandejasA=(huevosA//30)
    bandejasAA=(huevosA//24)
    bandejasAAA=(huevosA//12)
    bandejasBC=(huevosA//30)

    print(f"\ntipo_huevos:A numero_huevos: {huevosA} numero_bandejas: {bandejasA}")
    print(f"tipo_huevos:AA numero_huevos: {huevosAA} numero_bandejas: {bandejasAA}")
    print(f"tipo_huevos:AAA numero_huevos: {huevosAAA} numero_bandejas: {bandejasAAA}")
    print(f"tipo_huevos:BC numero_huevos: {huevosBC} numero_bandejas: {bandejasBC}")

    





def tipoHuevo(peso):
    try:
        if peso>=67:
            return "AAA"
        elif peso<67 and peso>=60:
            return "AA"
        elif peso>=53 and peso<60:
            return "A"
        elif peso<53 and peso>0:
            return "BC"
        else:
            peso=1/0
    except:
        print("HUBO UN ERROR AL CATEGORIZAR EL TIPO DE HUEVO. VUELVA A INTENTARLO")



nhuevos=int(input("INGRESE LA CANTIDAD DE HUEVOS QUE VA A INGRESAR: "))
contador=1
huevos=[]
for i in range(nhuevos):
    
    while True:
        try:
            peso=float(input(f"INGRESE EL PESO DEL HUEVO #{contador}: "))
            break
        except:
            print("HUBO UN ERROR, VUELVA A INTENTAR INGRESAR LA INFORMACION SOLICITADA.\n")
    huevos.append(tipoHuevo(peso))
    contador+=1
    
calcularBandeja(huevos)    
