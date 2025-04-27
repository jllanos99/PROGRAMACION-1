#Realizá un programa para ingresar 3 números  e  indique cuál de ellos es el mayor y su valor.

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))

if num_1 > num_2 and num_1 > num_3:
    msje = (f"El número mayor es:  {num_1}")
elif num_2 > num_3:
    msje = (f"El número mayor es:  {num_2}")
else:
    msje = (f"El número mayor es:  {num_3}")
print(msje) 
