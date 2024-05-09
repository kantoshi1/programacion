
peso = float(input("introuzca su peso en kg:"))
altura = float(input("introduzca su altura en metros:"))
IMC =  peso/ (altura ** 2)
if IMC < 18.5:
   Resultado = "Bajo peso"
elif IMC < 25 :
   Resultado = "Normal"
else :
   Resultado = "Sobrepeso"

print(f"Su IMC es {IMC:1f}. Usted tiene {Resultado}")