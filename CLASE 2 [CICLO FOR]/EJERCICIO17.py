#Realiza un programa que permita ingresar los sueldos de n empleados diferentes 
# (debe ingresar cuántos empleados quiere) . Calcular y mostrar el promedio de todas 
# los sueldos  ingresados y mostrar cuántos sueldos fueron mayor a 10000

suma_sueldos = 0 
sueldos_mayores = 0

cant_sueldos = int(input("Ingrese la cantidad de sueldos a cargar: "))

for i in range(cant_sueldos):
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    suma_sueldos += sueldo
    if sueldo > 10000:
        sueldos_mayores += 1

promedio = suma_sueldos / cant_sueldos
print (f"El promedio es: {promedio}")
print (f"La cantidad de sueldos mayores a 10000 es: {sueldos_mayores}")
