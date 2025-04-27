#Realiza un programa que permita al usuario ingresar 5 números enteros positivos, uno por uno. 
# El programa debe mostrar cada número ingresado. Si el usuario ingresa un número menor o igual a 0 , 
# el programa debe interrumpirse inmediatamente y mostrar un mensaje indicando que se ingresó un número 

for i in range(5):
    num = int(input("Ingrese un número entero positivo: "))
    if num <= 0:
        print("El numero es menor o igual a cero.")
        break
print ("fin")