#Para ingresar al parque temático Aventura en el aire, se requiere más de 12 años de edad o 
# medir más de 1,50 metros.El programa debe permitir ingresar la edad y la estatura , y 
# determinar si pueden ingresar o no a la atracción.

edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))
msje = ""   

if edad >= 12 and estatura > 1.50:
    msje = "Puede ingresar a la atraccion."
else:
    msje = "No puede ingresar a la atraccion."
print(msje)