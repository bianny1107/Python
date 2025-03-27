# Programa que enseña el uso del teorema de Pitágoras

import math

a = int(input("Inserte un valor: "))
b = int(input("Inserte otro valor: "))

total_a = a ** 2
total_b = b ** 2
suma = total_a + total_b
c = math.sqrt(suma) #sqrt es para sacar la raiz.

print(f"C mide {c}") #f sirve para concatenar valores en una cadena sin necesidad de convertirlo