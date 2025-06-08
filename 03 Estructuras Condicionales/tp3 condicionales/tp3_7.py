#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla. 
frase= input("Por favor ingrese una frase: ")
if frase [-1] == "a" or frase [-1] == "e" or frase [-1] =="i" or frase [-1] == "o" or frase [-1] == "u":
    print(f"{frase}!")
else:
    print(frase)








