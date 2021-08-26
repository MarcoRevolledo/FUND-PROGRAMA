def Calcularkilometros(num_inicial, n_dias): 
    acumulador=num_inicial
    dia=1
    dia_anterior=num_incial
    while dia!=n_dias:
        
        dia+=1
        if((dia%3)==0): 
            dia_anterior=(dia_anterior/2)
            acumulador=acumulador+dia_anterior
        else:
            dia_anterior=((dia_anterior*2)+10)
            acumulador=acumulador+dia_anterior
        print(f"EL ACUMULADO ES:{acumulador} EN {dia}")
        
    
    
num_incial=int(input("INGRESE LA CANTIDAD DE KILOMETROS RECORRIDOS EN UN SOLO DÍA: "))
n_dias=int(input("INGRESE LA CANTIDAD DE DIAS: "))
Calcularkilometros(num_incial,n_dias)
