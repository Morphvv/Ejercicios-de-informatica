pedido = {}
total = 0

while True:
    print("[1]: Agregar producto y su valor")
    print("[2]: Modificar el valor de un producto")
    print("[3]: Obtener el total")
    print("[4]: Salir")

    # Manejo de excepciones para la opción
    try:
        opcion = int(input("Ingrese su opción: "))
        if opcion not in [1, 2, 3, 4]:
            print("Opción no válida, por favor elija una opción entre 1 y 4.")
            continue
    except ValueError:
        print("Por favor, ingrese un número válido para la opción.")
        continue

    if opcion == 1:
        producto = input("Ingrese el producto: ").capitalize()
        try:
            precio = float(input(f"Ingrese el precio del {producto}: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intente nuevamente.")
                continue
            pedido[producto] = precio
            total += precio  # Sumar al total cada vez que se agrega un producto
        except ValueError:
            print("Por favor, ingrese un precio válido.")
    
    elif opcion == 2:
        busca_producto = input("Indique el producto a modificar: ").capitalize()
        if busca_producto in pedido:
            try:
                nuevo_valor = float(input("Ingrese el valor del producto: "))
                if nuevo_valor < 0:
                    print("El precio no puede ser negativo. Intente nuevamente.")
                    continue
                total -= pedido[busca_producto]  # Restamos el valor anterior
                pedido[busca_producto] = nuevo_valor  # Actualizamos el precio
                total += nuevo_valor  # Sumamos el nuevo valor al total
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el precio.")
        else:
            print(f"Producto {busca_producto} no encontrado.")
    
    elif opcion == 3:
        print("\nResumen de productos:")
        for producto, precio in pedido.items():
            print(f"{producto}: ${precio:.2f}")
        print(f"Total: ${total:.2f}")
    
    elif opcion == 4:
        print("\nResumen final de tu pedido:")
        for producto, precio in pedido.items():
            print(f"{producto}: ${precio:.2f}")
        print(f"Total final: ${total:.2f}")
        break

    # Pregunta si desea realizar otra acción
    respuesta = input("¿Desea realizar otra acción? [S/N]: ").capitalize()
    if respuesta == "N":
        print("Gracias por su compra.")
        break
