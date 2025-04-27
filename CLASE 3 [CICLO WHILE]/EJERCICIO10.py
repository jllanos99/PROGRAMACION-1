# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

minimo = 5
maximo = 10 
contador = 0
suma = 0 

while contador < minimo:
    numero = float(input("Ingrese un número: "))
    suma += numero
    contador += 1
