
import math
from shapely.geometry import Point, Polygon

def punto_dentro_triangulo(punto, vertices_triangulo):
    """
    Verifica si un punto está dentro de un triángulo.
    punto: (x, y)
    vertices_triangulo: [(x1, y1), (x2, y2), (x3, y3)]
    """
    punto_shapely = Point(punto)
    triangulo_shapely = Polygon(vertices_triangulo)
    return triangulo_shapely.contains(punto_shapely)

def circulo_dentro_triangulo(centro, radio, vertices_triangulo):
    """
    Verifica si un círculo está completamente contenido dentro de un triángulo.
    centro: (x, y)
    radio: radio del círculo
    vertices_triangulo: [(x1, y1), (x2, y2), (x3, y3)]
    """
    # Verificar si el centro del círculo está dentro del triángulo
    if not punto_dentro_triangulo(centro, vertices_triangulo):
        return False
    
    # Calcular los vértices del triángulo como puntos Shapely
    puntos_triangulo = [Point(v) for v in vertices_triangulo]
    
    # Verificar si algún vértice del triángulo está dentro del círculo
    for punto in puntos_triangulo:
        if punto.distance(Point(centro)) > radio:
            return False
    
    return True

# Ejemplo de uso
centro_circulo = (1, 0)
radio_circulo = 15
vertices_triangulo = [(8, 0), (3, 0), (1, 2)]

if circulo_dentro_triangulo(centro_circulo, radio_circulo, vertices_triangulo):
    print("El círculo está completamente contenido dentro del triángulo.")
else:
    print("El círculo no está completamente contenido dentro del triángulo.")
