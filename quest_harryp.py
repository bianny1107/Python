# Programa que elije a qué casa de magos perteneces

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Para que el sombrero elija correctamente, responda a todas las preguntas: \n")

print("Q1) ¿Prefieres el amanecer o el anocher? \n"
"   1. Amanecer \n"
"   2. Anochecer \n")

primera_res = int(input(": "))

if(primera_res == 1):
    gryffindor = gryffindor + 1
    ravenclaw = ravenclaw + 1
elif(primera_res == 2):
    hufflepuff = hufflepuff +1
    slytherin = slytherin + 1
else:
    print("Elección no válida")


print("Q2) Cuando esté muerto, quiero que la gente me recuerde como: \n"
"   1. El bueno \n"
"   2. El grande \n"
"   3. El sabio \n"
"   4. El audaz \n") 

segunda_res = int(input(": "))

if(segunda_res == 1):
    hufflepuff = hufflepuff + 2
elif(segunda_res == 2):
    slytherin = slytherin + 2
elif(segunda_res == 3):
    ravenclaw = ravenclaw + 2
elif(segunda_res == 4):
    gryffindor = gryffindor + 2
else:
    print("Elección no válida")


print("Q3) ¿Qué instrumento suena más placentero al oído?: \n"
"   1. El violín \n"
"   2. La trompeta \n"
"   3. El piano \n"
"   4. La batería \n") 

tercera_res = int(input(": "))

if(tercera_res == 1):
    slytherin = slytherin + 4
elif(tercera_res == 2):
    hufflepuff = hufflepuff + 4
elif(tercera_res == 3):
    ravenclaw = ravenclaw + 4
elif(tercera_res == 4):
    gryffindor = gryffindor + 4
else:
    print("Elección no válida")

print("\n Tabla de puntuaciones \n"
"----------------------- \n"
f"  Gryffindor = {gryffindor} \n"  
f"  Ravenclaw = {ravenclaw} \n"
f"  Hufflepuff = {hufflepuff} \n"
f"  Slytherin = {slytherin} \n")

if((gryffindor > ravenclaw) and (gryffindor > hufflepuff) and (gryffindor > slytherin)):
    print("El sombrero ha dictado que pertenece a la casa de Gryffindor.")
elif((ravenclaw > gryffindor) and (ravenclaw > hufflepuff) and (ravenclaw > slytherin)):
    print("El sombrero ha dictado que pertenece a la casa de Ravenclaw.")
elif((hufflepuff > ravenclaw) and (hufflepuff > gryffindor) and (hufflepuff > slytherin)):
    print("El sombrero ha dictado que pertenece a la casa de Hufflepuff.")
else:
    print("Resultado: El sombrero ha dictado que pertenece a la casa de Slytherin")