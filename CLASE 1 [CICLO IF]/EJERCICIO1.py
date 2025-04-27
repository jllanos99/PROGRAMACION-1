#Realizá un programa que permita ingresar 4 notas pertenecientes a cuatro bimestres distintos 
#para un alumno de secundaria. Debe calcularse y mostrarse la nota promedio. 

CANT_BIMESTRES = 4 

nota1 = float(input("Ingrese la nota del primer cuatrimestre: "))
nota2 = float(input("Ingrese la nota del segundo cuatrimestre: "))
nota3 = float(input("Ingrese la nota del tercer cuatrimestre: "))
nota4 = float(input("Ingrese la nota del cuarto cuatrimestre: "))

suma = nota1 + nota2 + nota3 + nota4
promedio = suma/ CANT_BIMESTRES
print(f"El promedio de las notas es: {promedio}")