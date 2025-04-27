#Para ingresar al concierto de la Banda “Pop Estelar” , se requiere tener al menos 10 años de edad 
# y medir más de 1,40 metros. El programa debe permitir ingresar la edad y la estatura de una persona 
# y determinar si pueden ingresar o no al concierto.

edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))
msje = ""

if edad >= 10 and estatura > 1.40:
    msje = "Puede ingresar al concierto."
else:
    msje = "No puede ingresar al concierto."
print(msje)