# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0 
suma = 0 

while True: #EL TRUE ES QUE NO SE SABE CUANTOS NÚMEROS SE VAN A INGRESAR
    # Se puede usar un break para salir del ciclo
    numero = float(input("Ingrese un número (o '0' para salir): "))
    if numero == 0:
        break
    suma += numero
    contador += 1 

if contador > 0:
    promedio = suma / contador
    print(f"El resultado de la suma es: {suma}")
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron números.")