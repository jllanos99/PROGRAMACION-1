#Ingresar 10 números enteros. Determinar el máximo y el mínimo.

maximo = 0
minimo = 0 
contador = 0 

while contador < 10:
    numero = int(input("Ingrese un número: "))
    if contador == 0:
        maximo = numero
        minimo = numero
    else:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    contador += 1

print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")