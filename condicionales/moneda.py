# Programa que permite girar una moneda para que salga un valor random

import random # Permite elegir un vaor random

num = random.randint(0, 1) # randint permite elegir un valor random entre 0 y 1.

if(num > 0.5): # Se pone 0.5 porque es el 50% de probabilidad de cara y el 50% de cruz
    print("Cara")
else:
    print("Cruz")