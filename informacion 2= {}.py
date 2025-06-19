informacion = {}

while True:
    print("\nMenú")
    print("1. Agregar usuario")
    print("2. Mostrar información de usuario")
    print("3. Eliminar usuario")
    print("4. Salir")
    
    # Opción del menú
    opcion = int(input("Seleccione su opción: "))
    
    if opcion == 1:
        # Agregar un usuario
        rut = int(input("Ingrese su RUT: \n"))
        nombre = input(f"Ingrese el nombre del usuario con RUT {rut}: \n").capitalize()
        fono = int(input(f"Ingrese el teléfono del usuario con RUT {rut}: \n"))
        mail = input(f"Ingrese el correo del usuario con RUT {rut}: \n").lower()
        fecha_nac = input(f"Ingrese la fecha de nacimiento del usuario con RUT {rut}: \n")
        
        # Guardar los datos en el diccionario
        informacion[rut] = [nombre, fono, mail, fecha_nac]
        print(f"Usuario con RUT {rut} agregado exitosamente.")
    
    elif opcion == 2:
        # Mostrar información de un usuario
        if len(informacion) == 0:
            print("No hay usuarios registrados.")
        else:
            print("\nLos usuarios registrados son:")
            for id in informacion:
                print(f"RUT: {id}")
            
            busca_id = int(input("Ingrese el RUT del usuario que desea buscar: \n"))
            
            if busca_id in informacion:
                print(f"Información del usuario con RUT {busca_id}:")
                print(f"Nombre: {informacion[busca_id][0]}")
                print(f"Teléfono: {informacion[busca_id][1]}")
                print(f"Correo: {informacion[busca_id][2]}")
                print(f"Fecha de nacimiento: {informacion[busca_id][3]}")
            else:
                print(f"No se encontró un usuario con el RUT {busca_id}.")
    
    elif opcion == 3:
        # Eliminar un usuario
        if len(informacion) == 0:
            print("No hay usuarios registrados.")
        else:
            print("\nLos usuarios registrados son:")
            for id in informacion:
                print(f"RUT: {id}")
            
            borrar_id = int(input("Ingrese el RUT del usuario que desea eliminar: \n"))
            
            if borrar_id in informacion:
                del informacion[borrar_id]
                print(f"Usuario con RUT {borrar_id} eliminado exitosamente.")
            else:
                print(f"No se encontró un usuario con el RUT {borrar_id}.")
    
    elif opcion == 4:
        # Salir
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")
