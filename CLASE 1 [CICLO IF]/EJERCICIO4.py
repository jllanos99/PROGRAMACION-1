#Realizá un programa que permita ingresar un número entero e indique si 
# se trata de un número par o impar. 

num = int(input("Ingrese un numero: "))

if num %2==0:
    print("El numero es par")
else:
    print("El numero es impar")