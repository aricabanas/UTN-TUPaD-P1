#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad_usuario= int(input("por favor ingrese su edad: "))
if edad_usuario < 12:
    print("Eres un niño.")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Eres un adolescente.")
elif edad_usuario >=18 and edad_usuario < 30:
    print("Eres un adulto joven.")
elif edad_usuario >= 30:
    print("Eres un adulto mayor.")
