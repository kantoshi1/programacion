Precio = 50 
Denominacion = [5 , 10 , 25]
ingresado = 0
adeudado = Precio

while adeudado > 0:
    moneda = int(input("Ingrese una moneda(5,10,25 centavos): "))
    if moneda in Denominacion :
        ingresado += moneda
        adeudado -= moneda
        print("Su monto adeudado es de {} centavos".format(adeudado))
    else:
        print("Moneda no aceptada. Ingrese una moneda de 5 , 10 , 25 centavos")

if ingresado > Precio:
    cambio = ingresado - Precio 
    print("Cambio: {} centavos".format(cambio))