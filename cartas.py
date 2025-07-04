cartas = {}

def agregar_carta():
    codigo = input("Ingrese el codigo de la carta: ")
    if codigo in cartas:
        print("La carta ya existe")
        return
    try:
        energia = int(input("Ingrese la energia inicial: "))
        if energia < 0:
            print("La energia no puede ser negativa.")
            return
        cartas[codigo] = {"estrellas": 0, "energia": energia, "uso_en_batalla": 0}
        print("Carta registrada correctamente.")
    except ValueError:
        print("Energia inválida. Debe ser un número entero.")

def usar_carta():
    codigo = input("Ingrese el codigo de la carta: ")
    if codigo not in cartas:
        print("Carta no registrada.")
        return
    try:
        total_energia = int(input("Ingrese la energia usada: "))
        if total_energia <= 0:
            print("Monto inválido.")
            return
        if cartas[codigo]["energia"] < total_energia:
            print("Energia insuficiente.")
            return
        cartas[codigo]["energia"] -= total_energia
        cartas[codigo]["uso_en_batalla"] += 1
        cartas[codigo]["estrellas"] += 1 
        print("Carta utilizada con éxito. Se ha sumado una estrella.")
    except ValueError:
        print("Energia inválida.")

def ver_energia_baja():
    try:
        minimo = int(input("Ingrese el mínimo de energia crítica: "))
        print("Cartas con energia crítica:")
        for num, datos in cartas.items():
            if datos["energia"] <= minimo:
                print(f"Carta {num} → Energia: {datos['energia']}")
    except ValueError:
        print("Ingrese un monto de energia válido.")

def lista_cartas():
    if not cartas:
        print("No hay cartas registradas.")
        return
    print("Listado de cartas:")
    for num, datos in cartas.items():
        print(f"Carta {num} → Energia: {datos['energia']}, Estrellas: {datos['estrellas']}, Usos en batalla: {datos['uso_en_batalla']}")

while True:
    print("Menu")
    print("[1] Agregar cartas")
    print("[2] Usar cartas")
    print("[3] Ver cartas con energia crítico")
    print("[4] Ver todas las cartas")
    print("[5] Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_carta()
    elif opcion == "2":
        usar_carta()
    elif opcion == "3":
        ver_energia_baja()
    elif opcion == "4":
        lista_cartas()
    elif opcion == "5":
        print("xao pescao")
        break
    else:
        print("Opción inválida. Intente nuevamente.")