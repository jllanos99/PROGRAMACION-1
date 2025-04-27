#Realizá un programa que permita al usuario ingresar un número entero entre 1 y 12. 
# Debe mostrarse por pantalla el nombre del mes que representa tal número, tomando el 1 
# como Enero y el 12 como Diciembre. Si el número ingresado está fuera de rango, debe mostrar "ERROR"

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

numero = int(input("Ingrese un número entre 1 y 12: "))
if 1 <= numero <= 12:
    print("El mes es:", meses[numero - 1])
else:
    print("ERROR")