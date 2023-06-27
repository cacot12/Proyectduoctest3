import random
salir=True
opcion=0
Autos={}
validar=False
while salir:
    print("Opción 1:Grabar\nOpción 2:Buscar \nOpción 3:Imprimir certificados\nOpción 4:Salir")
    opcion=input("Escoge una opción: ")
    while True:
        if len(opcion)==1:
            if opcion in "1234":
                opcion=int(opcion)
                break
        opcion=input("Escoge una opción valida: ")
    caracteristicas=[]
    multas=[]
    a=""
    if opcion==1:
        validar=True
        patente=input("ingrese una patente valida (entre 2 y 15): ")
        while True:
            if len(patente)>1 and len(patente)<16:
                break
            patente=input("ingrese una patente valida (entre 2 y 15): ")
        tipo=input("Ingrese el tipo del vehiculo: ")
        marca=input("Ingrese la marca del vehiculo: ")
        precio=(input("Ingrese precio del vehículo: "))
        while True:
            if precio=="":
                precio=(input("Ingrese precio valido del vehículo (Mayor a 5 millones): "))
            else:
                c=0
                for t in precio:
                    if t in "0123456789":
                        c+=1
                    else:
                        precio=(input("Ingrese precio valido del vehículo (Mayor a 5 millones): "))
                        break
                    if c==len(precio):
                        precio=int(precio)
                if isinstance(precio,int):
                    if precio >5000000:
                        break
                    precio=(input("Ingrese precio valido del vehículo (Mayor a 5 millones): "))
        print("¿Tiene multas? \n1.-Si\n2._No")
        while True:
            a=input()
            if a=="1":
                multas.append((random.randrange(1500,3000),input("Ingrese fecha de la multa: ")))
            elif a=="2":
                if multas==[]:
                    multas.append("No posee multas")
                break
            else:
                print("Marque una opción Valida ( '1' o '2'): ")
            print("¿Tiene más multas? \n1.-Si\n2._No")
        fecha_registro=input("Ingrese fecha de registro del vehículo: ")
        dueño=input("ingrese el dueño del vehículo: ")
        caracteristicas.append(tipo)
        caracteristicas.append(marca)
        caracteristicas.append(precio)
        caracteristicas.append(multas)
        caracteristicas.append(fecha_registro)
        caracteristicas.append(dueño)
        Autos[patente]=caracteristicas
    if opcion==2 and validar:
        busqueda=input("ingrese una patente previamente registrada: ")
        while True:
            if busqueda in Autos:
                break
            busqueda=input("ingrese una patente previamente registrada: ")
        print(Autos[busqueda])
    if opcion==3 and validar:
        busqueda=input("ingrese una patente previamente registrada: ")
        while True:
            if busqueda in Autos:
                break
            busqueda=input("ingrese una patente previamente registrada: ")
        print("\n\nCertificados de Emisión de contaminantes\n\n\nPatente: ",busqueda,"\nDueño: ",Autos[busqueda][5],"\nFecha del registro: ", Autos[busqueda][4],"\nMultas: ")
        for q,w in Autos[busqueda][3]:
            print("$",q,"El día: ",w)
    if opcion==4:
        break
    if not validar:
        print("**********************    **********************\n**********************    **********************\n   Debe grabar primero un Registro de vehículo\n**********************    **********************\n**********************    **********************\n")


