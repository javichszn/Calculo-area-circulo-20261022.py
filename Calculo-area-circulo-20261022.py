# Definimos la función del area del circulo "π*r**2"
import math 
def area_ciculo(radio):


    """
    Función del area del circulo

    Parametros:
    - No importa en que unidades se da

    Devuelve:
    - Area en la unidad que se da ( cm^2; m^2; km^2; etc)
    """
    area = math.pi * (radio**2)
    return area 

#pedir los datos de entrada
radio = int(input("Introduzca la longitud del radio en cualquier unidad: "))
area = area_ciculo(radio)
area = round(area, 2)

print(f"El área del cirulo es {area} ")