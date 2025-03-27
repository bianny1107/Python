# Programa de bola Magic 8

import random

respuestas =  [ # Esta es una lista y se escribe con corchetes, se puede modificar después de haber sido creadas (son mutables).
 "Sí, definitivamente", 
 "Ya está decidido", 
 "Sin dudarlo", 
 "Respuesta borrosa, inténtalo de nuevo", 
 "Pregunta más tarde de nuevo", 
 "Mejor no te digo ahora", 
 "Mis fuentes dicen que no", 
 "El resultado no es bueno", 
 "Muy dudoso"  
 ]

pregunta = input("Haga su pregunta: ")
eleccion = random.choice(respuestas)

print(f"Magic 8 Ball: {eleccion}")