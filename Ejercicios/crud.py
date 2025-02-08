nevera = []
congelador = []


while True:
    print("By: Dajachi")
    print("\n## MENU ##")
    print("\n1.Agregar elemento")
    print("2.Ver elementos")
    print("3.Eliminar elemento")
    print("0.Salir")
    
    opcion = input("\nIngrese el número de la opción: ")
    
    # Opción 1
    if opcion == "1":
        eleccion = input("\nAgregar a:\n1.Congelador\n2.Nevera\n\nOpción: ")
        
        # sub-opcion 1
        if eleccion == "1":
            producto = input("\nNombre: ")
            try:
                cantidad = int(input("Cantidad: "))
        
                congelador.append((producto, cantidad))
                print(f"\nEl elemento '{producto}' se agrego al Congelador.")
                input("\n¡Enter para continuar!\n")
            
            except ValueError:
                print("\n¡Debes digitar un número entero!")
        
        # sub-opcion 2
        elif eleccion == "2":
            producto = input("\nNombre: ")
            try:
                cantidad = int(input("Cantidad: "))
            
                nevera.append((producto, cantidad))
                print(f"\nEl producto '{producto}' se agrego al Nevera.")
                input("\n¡Enter para continuar!\n")
                
            except ValueError:
                print("\n¡Debes digitar un número entero!")
        
        else:
            print("\n¡Esa opción no existe!")
            input("\n¡Enter para continuar!\n")
    
    # Opción 2
    elif opcion == "2":
        eleccion = input("\nVer elemento de:\n1.Congelador\n2.Nevera\n\nOpción: ")
        
        # sub-opcion 1
        if eleccion == "1":
            # comprobar si hay elmentos en el congelador
            if congelador:
                print("\nElementos:")
                for i in congelador:
                    print(f"\nNombre: {i[0]}")
                    print(f"Cantidad: {i[1]}")
                    
                input("\n¡Enter para continuar!\n")
            
            else:
                print("\nNo hay nada que mostrar.")
                input("\n¡Enter para continuar!\n")
        
        # sub-opcion 2
        elif eleccion == "2":
            # comprobar si hay elmentos en la nevera
            if nevera:
                print("\nElementos:")
                for i in nevera:
                    print(f"\nNombre: {i[0]}")
                    print(f"Cantidad: {i[1]}")
                    
                input("\n¡Enter para continuar!\n")
            
            else:
                print("\nNo hay nada que mostrar.")
                input("\n¡Enter para continuar!\n")

    # Opción 3
    elif opcion == "3":
        eleccion = input("\nEliminar elemento de:\n1.Congelador\n2.Nevera\n\nOpción: ")
        
        # sub-opcion 1
        if eleccion == "1":
            if congelador:
                nombre_elemento = input("\nNombre del elemento a eliminar: ")
                for elemento in congelador:
                    if elemento[0] == nombre_elemento:
                        congelador.remove(elemento)
                print(f"\nEl elemento '{nombre_elemento}' se ha eliminado del Congelador.")
            
            else:
                print("\nNo hay nada que mostrar.")
                input("\n¡Enter para continuar!\n")
    
    # Opción 4
    elif opcion == "0":
        print("\nGracias por utilizar el programa.")
        break

    else:
        print("¡Esa opción no existe!")
        input("\n¡Enter para continuar!\n")
            