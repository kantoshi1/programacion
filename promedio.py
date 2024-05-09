
grades = []
while True :
    grade = input("inserte una calificacion (o 'salir' para terminar)")
    if grade.lower()=="salir":
        break
    else:
        grades.append(float(grade))


average= sum(grades)/len(grades)
print(" el promedio de las notas fue: ", average) 