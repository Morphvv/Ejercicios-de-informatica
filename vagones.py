cant_vag = int(input("Cuantos vagones quiere llevar: "))
while cant_vag < 1 or cant_vag >10:
    print("La cantidad ingresada no es valida, tiene que ser menor a 10 y mayor a 0")
    cant_vag = int(input("Ingrese una cantidad valida: "))
    
costo_transporte = cant_vag * 75000
costo_productos = 0 
cont_maiz = 0
cont_trigo = 0
cont_cebada = 0
cont_porotos = 0
cont_lentejas = 0

for i in range(cant_vag):
    print ("Ingrese un producto")
    print("[1]: Maiz. 15.000$")
    print("[2]: Trigo. 13.000$")
    print("[3]: Cebada. 10.000")
    print("[4]: Porotos. 18.000$")
    print("[5]: Lentejas. 20.000$")
    
    producto = int(input("Indique el producto a transportar: "))
    if producto == 1:
        precio_producto = 15000
        tipo_producto = "Maiz"
    elif producto == 2 :
        precio_producto = 13000
        tipo_producto = "Trigo"
    elif producto == 3:
        precio_producto = 10000
        tipo_producto = "Cebada"
    elif producto == 4:
        precio_producto = 18000
        tipo_producto = "Porotos"
    elif producto == 5:
        precio_producto = 20000
        tipo_producto = "Lentejas"
        
    contenedores = int(input(f"Indique la cantidad de contenedores para el vagón{i+1}:"))
    if producto == 1:
        cont_maiz = cont_maiz + contenedores
    elif producto == 2:
        cont_trigo = cont_trigo + contenedores
    elif producto == 3:
        cont_cebada = cont_cebada + contenedores
    elif producto == 4:
        cont_porotos = cont_porotos + contenedores
    elif producto == 5:
        cont_lentejas = cont_lentejas + contenedores
        
    costo_productos = costo_productos + contenedores * precio_producto
    total = costo_productos + costo_transporte
    
print(f"Usted solicito  {cant_vag} de vagones, transportando {tipo_producto}, con un total de contenedores de {contenedores} el coso total a transportar {costo_transporte}, y el costo de contenedor {costo_productos}. Con un total de {total}")

