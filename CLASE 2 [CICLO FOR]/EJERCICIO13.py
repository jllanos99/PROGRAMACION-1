#Desarrolla un programa que solicite al usuario ingresar dos valores enteros: inicio y fin.  
# Asegúrate de que inicio sea menor o igual que fin. 
# Luego, el programa debe: Mostrar todos los números desde inicio hasta fin inclusive. 
# Mostrar todos los números entre inicio y fin, excluyendo los extremos.

inicio = int(input("Ingrese un numero entero: "))
fin = int(input("Ingrese un segundo numero: "))

if inicio <= fin:
    print ("Extremos incluidos")
    for i in range(inicio, fin + 1):
        print (i)
else:
    print ("Ingreso incorrecto.")