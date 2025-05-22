trabajadores = int(input("Ingrese cuantos trabajadores hay registrados: "))
while trabajadores < 0:
    print("Tiene que ser un numero positivo, ingrese de nuevo la cantidad")
    trabajadores = int(input("Ingrese cuantos trabajadores hay registrados: "))
else:
    print("Cantidad valida")
cap_lista = 0
cap_nolista = 0
for i in range(trabajadores):
    modulos = int(input(f"Ingrese la cantidad de modulos capacitados realizados por el trabajador {i+1}:  "))
    if modulos >= 4:
        cap_lista = cap_lista + 1
    else:
        cap_nolista = cap_nolista + 1
print(f"Usted tiene {trabajadores} trabajadores.")
print(f"{cap_lista} estan capacitados.")
print(f"{cap_nolista} que no estan capacitados.")