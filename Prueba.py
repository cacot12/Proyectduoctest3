import random
salir=True
opcion=0
Autos={}
while salir:
    print("Opción 1:Grabar\nOpción 2:Buscar \nOpción 3:Imprimir certificados\nOpción 4:Salir")
    opcion=int(input("Escoge una opción: "))
    while opcion >4 or opcion <1 :
        print("Digite una Opción valida\nOpción 1:Grabar\nOpción 2:Buscar \nOpción 3:Imprimir certificados\nOpción 4:Salir")
        opcion=int(input("Escoge una opción valida: "))
    caracteristicas=[]
    multas=[]
    a=""
    if opcion==1:
        patente=input("ingrese una patente valida (entre 2 y 15): ")
        while True:
            if len(patente)>1 and len(patente)<16:
                break
            patente=input("ingrese una patente valida (entre 2 y 15): ")
        tipo=input("Ingrese el tipo del vehiculo: ")
        marca=input("Ingrese la marca del vehiculo: ")
        precio=int(input("Ingrese precio del vehículo: "))
        while True:
            if precio >5000000:
                break
            precio=int(input("Ingrese precio del vehículo: "))
        print("¿Tiene multas? \n1.-Si\n2._No")
        while True:
            a=int(input())
            if a==1:
                multas.append((random.randrange(1500,3000)))
                multas.append(input("Ingrese fecha de la multa"))
            elif a==2:
                if multas==[]:
                    multas.append("No posee multas")
                break
            else:
                print("Marque una opción Valida: ")
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
    if opcion==2:
        busqueda=input("ingrese una patente valida (entre 2 y 15): ")
        while True:
            if len(busqueda)>1 and len(busqueda)<16:
                break
            busqueda=input("ingrese una patente valida (entre 2 y 15): ")
        print(Autos[busqueda])
    if opcion==3:
        busqueda=input("ingrese una patente valida (entre 2 y 15): ")
        while True:
            if len(busqueda)>1 and len(busqueda)<16:
                break
            busqueda=input("ingrese una patente valida (entre 2 y 15): ")
        print("Certificados de Emisión de contaminantes\nPatente ",busqueda,"\nDueño: ",Autos[busqueda][5],"\nFecha del registro: ", Autos[busqueda][4],"\nMultas: ",Autos[busqueda][3])
    if opcion==4:
        salir=False
