nombre = input("Ingrese su nombre completo: ")
nota1 = float(input(""))
nota2 = float(input(""))
nota3 = float(input(""))
nota_presentacion = (nota1 * 0.25 + nota2 * 0.30 + nota3* 0.45) 

if nota_presentacion > 5.0:
    print (f"Hola {nombre}, sus notas fueron {nota1} {nota2} {nota3}. Su puntaje puntaje final fue {nota_presentacion}. Usted aprobo.")
else:
    print ("Usted debera rendir una prueba extra, ingrese el valor de la nota extra.")
    nota_extra = float(input(""))
    nota_final = nota_extra * 0.40 + nota_presentacion * 0.60
if nota_final < 4.0:
    print (f"Hola {nombre}, sus notas fueron {nota1} {nota2} {nota3} y {nota_extra}. Su puntaje puntaje final fue {nota_final}. Usted reprobo.")
else:
    print (f"Hola {nombre}, sus notas fueron {nota1} {nota2} {nota3} y {nota_extra}. Su puntaje puntaje final fue {nota_final}. Usted aprobo.")