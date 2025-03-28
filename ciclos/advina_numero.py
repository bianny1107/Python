# Programa en el que el usuario trata de adivinar un número
valor = 0
intento = 0
while(valor != 6 and intento < 3):
    valor = int(input("Adivina el número...... "))
    intento = intento  + 1

    if(valor == 6):
        print("\n ¡Lo conseguiste ;) ! \n")
    elif(intento != 3):
        print("\n Sigue intentándolo :| \n")
    else:
        print("\n ¡Fallaste :( ! Inténtalo más tarde.")
        break