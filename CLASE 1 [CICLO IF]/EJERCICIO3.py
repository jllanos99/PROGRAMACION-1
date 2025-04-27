#Realizá un programa que permita ingresar dos número. Debes mostrar los resultados para las 4 
# operaciones matemáticas básicas con los números ingresados. No debe permitir la división por 0.

num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))

suma = num_1 + num_2
resta = num_1 - num_2
multiplicacion = num_1 * num_2

if num_2 != 0:
    division = num_1 / num_2

print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")
if num_2 != 0:
    print(f"El resultado de la division es: {division}")
else:
    print("No se puede dividir por 0")