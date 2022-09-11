Lista=[]
def menú():
    print ("Bienvenido a este creador de protocolos:)\n\
           Inserta la opción que deseas\n\
           1.Inserta el nombre del protocolo\n\
           2.Añadir un paso\n\
           3.Paso en posicion indicada (usar en caso de haber borrado un paso, selecciona si necesitas mas informacion) \n\
           4.Mostrar protocolo completo\n\
           5.Borrar un elemento\n\
           6.Agregar subpaso\n\
           7.Salir")
    print ("--------------------------------------------------------------------------------")
while True:
    menú()
    opStr=input( )
    if opStr.isnumeric()==False:
        print("opción invalida")
    else:
        opcion = int(opStr)

        if opcion ==1:
            Nombre = str(input("Escribe el nombre del protocolo a crear: "))

        elif opcion == 2:
            Paso = int(input("Paso No.: "))
            Redactado = str(input("Escribe el paso de protocolo: "))
            Lista.append([Paso, Redactado])

        elif opcion == 3:
            posicion = int(input("(si borraste anteriormente un paso habras notado que los pasos no tienen continuidad y falta el numero de paso que borraste,puedes solucionarlo en esta opcion poniendo la posicion del elemento que borraste,asi como el numero de paso que era y su nuevo contenido)"))
            Paso = int(input("Paso No.: "))
            Redactado = str(input("Escribe el paso de protocolo: "))
            Lista.insert(posicion,[Paso, Redactado])
            
        elif opcion == 4:
            print("Nombre de tu protocolo: "+ Nombre)
            print("Los pasos de tu protocolo son: ")
            for i in Lista:
                print (i)

        elif opcion == 5:
            bor = int (input ("Escribe la posicion del paso que deseas borrar,teniendo en cuenta que dentro de esta lista el primer paso será 0 y se considerará dentro de la misma a los subpasos: "))
            Lista.pop(bor)
            print("Se ha borrado este paso")

            if bor!=None:
                print ("Elemento no encontrado")

        elif opcion == 6:
            posicion = int(input("Escribe la posicion del paso al cual le quieres agregar el subpaso,teniendo en cuenta que dentro de esta lista el primer paso será 0"))
            Subpaso = (input("Subpaso No.(Numera el subpaso asi: EJEMPLO: si el paso es no.1 tu subpaso será 1.1): "))
            Redactado = str(input("Escribe el paso de protocolo: "))
            Lista.insert(posicion,[Subpaso, Redactado])

        elif opcion == 7:
            print ("Hasta luego:)")
            break

        else:
            print ("opcion no valida")









            
                
