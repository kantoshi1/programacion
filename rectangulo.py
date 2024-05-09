import math

def area_cono(radio, altura):
    """
    Calcula el área superficial de un cono dado su radio y altura.
    """
    area_base = math.pi * radio**2
    area_lateral = math.pi * radio * math.sqrt(radio**2 + altura**2)
    return area_base + area_lateral

def area_dos_conos(radio1, altura1, radio2, altura2):
    """
    Calcula el área total de dos conos.
    """
    area_cono1 = area_cono(radio1, altura1)
    area_cono2 = area_cono(radio2, altura2)
    return area_cono1 + area_cono2

# Ejemplo de uso
radio_cono1 = 5
altura_cono1 = 10
radio_cono2 = 2
altura_cono2 = 25

area_total = area_dos_conos(radio_cono1, altura_cono1, radio_cono2, altura_cono2)
print("El área total de los dos conos es:", area_total)
