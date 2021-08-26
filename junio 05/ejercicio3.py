def sumar(n1,n2):
    return n1+n2

def restar(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1-n2

def dividir(n1,n2):
    return n1-n2







while True:
    print("1- SUMA\n2- RESTA\n3- MULTIPLICACION\n4- DIVISION\n6- SALIR")
    e=int(input("\nINGRESE SU OPCION: "))
    if(e==1):
        while True:
            try:
                print("\n\nSUMA")
                n1,n2=int(input("INGRESE EL NUMERO 1: ")),int(input("INGRESE EL NUMERO 2: "))
                print(f"LA SUMA:{sumar(n1,n2)}\n")
                break
            except (ValueError, TypeError):
                print("INGRESE VALORES CORRECTOS\n")
    elif(e==2):
        while True:
            try:
                print("\n\nRESTA")
                n1,n2=int(input("INGRESE EL NUMERO 1: ")),int(input("INGRESE EL NUMERO 2: "))
                print(f"LA RESTA ES:{restar(n1,n2)}\n")
                break
            except (ValueError, TypeError):
                print("INGRESE VALORES CORRECTOS\n")
            except(ZeroDivisionError):
                print("No se puede dividir entre 0")
    elif(e==3):
        while True:
            try:
                print("\n\nMULTIPLICACION")
                n1,n2=int(input("INGRESE EL NUMERO 1: ")),int(input("INGRESE EL NUMERO 2: "))
                print(f"LA MULTIPLICACION:{multiplicar(n1,n2)}\n")
                break
            except (ValueError, TypeError):
                print("INGRESE VALORES CORRECTOS\n")
    elif(e==4):
        while True:
            try:
                print("\n\nDIVISION")
                n1,n2=int(input("INGRESE EL NUMERO 1: ")),int(input("INGRESE EL NUMERO 2: "))
                print(f"LA DIVISION:{dividir(n1,n2)}\n")
                break
            except (ValueError, TypeError):
                print("INGRESE VALORES CORRECTOS\n")
    elif(e==6):
        print("\n\nUSTED SALIO EXITOSAMENTE!!!")
        break
    else:
        print("\n\nINGRESE UNA OPCION CORRECTA")
    