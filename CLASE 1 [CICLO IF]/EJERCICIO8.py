#Realizá un programa que permita ingresar una edad (entre 1 y 120 años) y un género 
# ('F' para mujeres, 'M' para hombres) de una persona interesada en aplicar para un viaje de grupos. 
# En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal 
# situación y terminar el programa. Si los datos están bien ingresados, el programa debe indicar si 
# la persona está en el rango de edad permitido para aplicar al viaje de grupos:Las mujeres pueden 
# aplicar entre los 20 y 55 años inclusive. Los hombres pueden aplicar entre los 25 y 51 años inclusive.
# Si la persona está dentro del rango de edad correspondiente según su género, podrá aplicar al viaje; 
# si no, no podrá hacerlo.

edad = int(input("Ingrese su edad (entre 1 y 120 años): "))
genero = input("Ingrese su género (F para mujeres, M para hombres): ")

if edad >= 1 and edad <= 120:
    if genero == 'F' or genero == 'M':
        if genero == 'F':
            if edad >= 20 and edad <= 55:
                print("Puede aplicar al viaje.")
            else:
                print("No puede aplicar al viaje.")
        elif genero == 'M':
            if edad >= 25 and edad <= 51:
                print("Puede aplicar al viaje.")
            else:
                print("No puede aplicar al viaje.")
        else:
            print("Género inválido. Programa terminado.")
    else:
        print("Edad fuera de rango. Programa terminado.")
else:
    print("Edad fuera de rango. Programa terminado.") 