#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
#edad_usuario=int(input("Por favor ingrese su edad: "))
#if edad_usuario >= 18:
#7    print("Es mayor de edad")
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
nota=int(input("Por favor ingrese su nota: "))
NOTA_MINIMA=6
if nota >= NOTA_MINIMA:
    print("APROBADO")
else:
    print("DESAPROBADO")
print()