cantidad_num = int(input("Ingrese la cantidad de numeros: "))
suma = 0
for i in range(cantidad_num):
    print("Los numeros no deben ser mayor a 100")
    num= int(input(f"Ingrese el numero {i+1} : "))
    suma += num
promedio = suma / cantidad_num

print(f"La cantidad de numeros ingresados es {cantidad_num}, y la suma de todos ellos es de {suma}, con un promedio de  {promedio}")