# Solicitar la cantidad de contraseñas a ingresar
cantidad_contra = int(input("Cuántas contraseñas desea ingresar: "))

# Inicializar contadores
aprobado = 0
reprobado = 0

# Ingresar y evaluar cada contraseña
for i in range(cantidad_contra):
    contraseña = input(f"Ingrese su contraseña {i + 1}: ")

    # Evaluar la longitud de la contraseña
    if 5 <= len(contraseña) <= 10:
        aprobado += 1
    else:
        reprobado += 1

# Mostrar resultados
print(f"\nLas contraseñas que sí cumplen son {aprobado}, y las que no cumplen son {reprobado}.")
