

camel_case = input("Ingrese un nombre de variable en camel case: ")

snake_case = " "


for i in range(len(camel_case)):
    
   if camel_case[i].isupper():
       
      snake_case += "_" + camel_case[i].lower()

   else:
       
      snake_case += camel_case[i]

print("el nombre de la variable en snake_case es:", snake_case)