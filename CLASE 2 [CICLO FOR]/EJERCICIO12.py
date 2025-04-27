#Realiza un programa que permita ingresar un número entero n. 
# Debe mostrar los primeros 5 múltiplos de n (desde 1 × n hasta 5 × n).

n = int (input("Ingrese un número entero: "))
for i in range (1,6):
    print (i *n) 