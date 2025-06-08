# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre=input("Por favor ingrese su nombre: ")
opcion = input(
    "Ingrese una opción:\n"
    "1 - Convertir a MAYÚSCULAS\n"
    "2 - Convertir a minúsculas\n"
    "3 - Convertir la Primera letra en mayúscula\n"
    "Opción: ")
if opcion == "1":
    print ("Tu nombre en MAYUSCULA es:", nombre.upper())
elif opcion == "2":
    print("Tu nombre en minuscula es:", nombre.lower())
elif opcion == "3":
    print("Tu nombre con la primera letra en mayuscula:", nombre.title())







