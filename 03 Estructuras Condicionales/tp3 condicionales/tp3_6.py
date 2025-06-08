#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla




#impoortamos las librerias necesarias y definimos el rango

import random
from statistics import mean, median, mode

#Generamos una lista de 50  numeros alestorios del 1 al 100

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#aca hacemos la media, mediana, y moda 

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#aca mostramos los resultados

print("Lista de números aleatorios:")
print(numeros_aleatorios)
print("\nMedia:", media)
print("Mediana:", mediana)
print("Moda:", moda)

#determinar el tipo de sesgo 

if media > mediana and mediana > moda:
    print("\n→ Hay sesgo POSITIVO (a la derecha).")
elif media < mediana and mediana < moda:
    print("\n→ Hay sesgo NEGATIVO (a la izquierda).")
elif media == mediana == moda:
    print("\n→ No hay sesgo (distribución simétrica).")
else:
    print("\n→ La distribución no sigue un patrón claro de sesgo.")




