#Hacemos el random en si
from random import randint
rango1 = randint(1 , 10)
rango2 = randint(11 , 20)
rango3 = randint(21 , 30)
#Definimos las variables modificables por el usuario
print("Es un juego de azar entre 3 rangos, deberas apostar, si usted acerta en los 3 rangos se triplicara su apuesta, si aciertas dos se duplicara, y si aciertas un solo numero tendras el 50 de la apuesta")
nombre = input("Ingrese su nombre: ")
valor_apuesta = int(input("Ingrese el valor de su apuesta: "))
num1_rango = int(input("Ingrese el primer numero del 1 al 10: "))
num2_rango = int(input("Ingrese el segundo numero del 11 al 20: "))
num3_rango = int(input("Ingrese el tercer numero del 21 al 30: "))
#Hacemos un contador de aciertos para ver cuantas veces el usuario acerta entre todos los rangos
aciertos = 0
if num1_rango == rango1:
    aciertos += 1
if num2_rango == rango2:
    aciertos += 1
if num3_rango == rango3:
    aciertos +=1
#Y con el contador de aciertos vamos variando el resultado  
if aciertos == 3:
    total = valor_apuesta * 3
elif aciertos == 2:
    total = valor_apuesta * 2
elif aciertos == 1:
    total = valor_apuesta * 1.5
else:
    total = valor_apuesta
    
print(f"Hola {nombre}, usted acerto una cantidad de {aciertos}, ganando un total de {total}")