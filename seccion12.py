lista=[]
snota=0
menor=5
mayor=0
iteracion=1
n=int(input("Digite el numero de estudiantes de la lista: "))
for i in range (n):
    while True:
        try:
            nota=float(input(f"Digite la nota del estudiante N°{iteracion}: "))
            if nota>5:
                print("Usted Ingreso una nota mayor a la permitida, se tomara el valor mas cercano que es 5.0")
                nota=5.0
            elif nota<0:
                print("Usted Ingreso una nota menor a la permitida, se tomara el valor mas cercano que es 0.0")
                nota=0.0
            break
        except (ValueError, TypeError):
            print("Ingrese las notas nuevamente de forma correcta")
    iteracion+=1
    lista+=[nota]



for i in lista:
    snota+=i
    if i < menor:
        menor = i
    if i > mayor:
        mayor = i

prom= snota/n
print("\nEl promedio del curso es: ",prom)
print("\nLa nota mayor es: ", mayor)
print("\nLa nota menor es: ", menor)