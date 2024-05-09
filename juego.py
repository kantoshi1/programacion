import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    intentos = 0
    
    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100. ¡Adivina cuál es!")
    
    while True:
        intento = int(input("Introduce tu suposición: "))
        intentos += 1
        
        if intento < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número es menor. Intenta de nuevo.")
        else:
            print(f"Felicidades, ¡adivinaste el número en {intentos} intentos!")
            break

# Llamamos a la función para comenzar el juego
juego_adivinanza()
