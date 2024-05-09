def main():
    shopping_lista = []

    while True:
        print("\n---Lista de compras---")
        print(" 1. Agregar articulo ")
        print(" 2. Eliminar articulo ")
        print(" 3. Ver lista ")
        print(" 4. Salir ")

        option = input("Porfavor introduzca una opcion: ")
        
        if option == "1":
           item = input("Introduzca un articulo que quiera agregar:  ")
           shopping_lista.append(item)
        elif  option == "2":
           item = input("Introduzca el articulo que quiera eliminar de la lista:  ")
           if item in shopping_lista:
              shopping_lista.remove(item)
        elif  option == "3":
           print("\n---Lista de compras---")
           for item in shopping_lista:
               print("-" + item)
        elif option == "4" :
           break
        
        else:
           print("Opcion invalida, porfavor intentar de nuevo")

if __name__ == "__main__":
       main ()    




 


