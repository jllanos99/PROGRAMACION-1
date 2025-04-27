#Realiza un programa que permita dibuje una matriz de asteriscos (*) de 4 de alto por 5 de ancho.   

ancho = 5
alto = 4 

for i in range(alto):
    for j in range(ancho):
        print("*", end=" ")
    print() 