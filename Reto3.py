'''
La empresa de acuadecto, desea calcular el valor recaudado por consumo de los clientes, si se tiene en cuenta lo siguiente:
- Debe capturar la direccion del cliente
- Debe calcular el valor a pagar por el cliente (Consumo*vrmetro)+iva
- Se cobra IVA de 10% por el consumo
- El estrato 5 paga un impuesto adicional de $2000
- Se debe tener en cuenta las siguientes tablas segun el estrato

Estrato    Valor Metro3
1              $3.000
2              $4.000
3              $5.000
4              $7.000
5              $10.000

La lista termina cuando el estrato es 0
Se busca generar las excepciones del estrato

'''

def tarifaBasica(numero):
    if(numero==1):
        return 3000
    elif(numero==2):
        return 4000
    elif(numero==3):
        return 5000
    elif(numero==4):
        return 7000
    elif(numero==5):
        return 10000
    else:
        return "Usted ingreso un estrato fuera de rango"

def impuesto(consumo, e):
    imp=consumo*0.1 
    if(e==5):
        imp+=2000
    return imp

def totalPagar(consumo, e):
    subtotal=(consumo*tarifaBasica(e))
    imp=impuesto(subtotal,e)
    total=subtotal+imp
    return total
    
e='1'
listaClientes=[]
while True:
    
    e=int(input("\nINGRESE EL ESTRATO: "))
    if(e==0):
        break
    else:
        direccion=input("INGRESE LA DIRECCION DEL HOGAR: ")
        nombre=input("INGRESE EL NOMBRE DEL CLIENTE: ")
        consumo=float(input(f"INGRESE EL CONSUMO DEL Sr(a).{nombre}: "))
        total=totalPagar(consumo, e)
        cliente=[nombre,direccion,e,consumo,total]
        listaClientes.append(cliente)
    
for i in listaClientes:
    print(f"\nNOMBRE CLIENTE: {i[0]}\nDIRECCION: {i[1]}\nESTRATO: {i[2]}\nCONSUMO: {i[3]}\nTOTAL A PAGAR{i[4]}\n ")
    
    
    

