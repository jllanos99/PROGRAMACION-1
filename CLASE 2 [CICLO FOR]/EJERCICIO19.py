#Realiza un programa que solicite al usuario ingresar su edad.
# El programa debe validar que la edad esté dentro del rango válido de 1 a 100 inclusive. 
# Si el valor ingresado no es válido, se debe pedir nuevamente hasta que el usuario ingrese  
# una edad correcta.

edad = int(input("Ingrese su edad: "))

if edad < 1 or edad >100:
    if edad < 1 or edad > 100:
        print("Edad no válida. Debe estar entre 1 y 100.")
        edad = int(input("Ingrese su edad nuevamente: "))
print(f"Su edad es de {edad} años") 