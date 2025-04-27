#Realiza un programa que permita al usuario ingresar un número entero positivo. 
# El programa debe mostrar en pantalla todos los números enteros desde 1 hasta ese número, 
# saltando los números pares (es decir, solo debe mostrar los impares).

numero = int(input("Ingrese un número entero positivo: "))
for i in range(1, numero, +1):
    if i %2!=0:
        print(i)
