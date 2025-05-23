alumnos_total = int(input("Ingrese la cantidad de alumnos: "))
aprobados = 0
reprobados = 0
suma_notas = 0

for i in range(alumnos_total):
    while True:
        try:
            nota_promedio = float(input(f"Ingrese la nota promedio del estudiante {i + 1} : "))
            if 1.0 <= nota_promedio <= 7.0:
                break  # Si la nota es válida, salir del bucle
            else:
                print("Nota fuera de rango. Debe estar entre 1.0 y 7.0.")
        except ValueError:
            print("Por favor ingrese un valor numérico válido.")
    
    suma_notas += nota_promedio
    
    if nota_promedio >= 4.0:
        aprobados += 1
    else:
        reprobados += 1

promedio = round(suma_notas / alumnos_total, 1)

print(f"La cantidad de alumnos ingresados es {alumnos_total}, la nota promedio entre todos es de {promedio}, con una cantidad de aprobados {aprobados}, y reprobados de {reprobados}")
