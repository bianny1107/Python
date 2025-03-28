# Programa que mide el nivel ph de un líquido

ph = int(input("Inserte el nivel de ph del líquido: "))

if(ph >= 0 and ph <= 14):
    if(ph > 7):
        print("El ph del líquido es básico")
    else:
        print("El ph del líquido es ácido")
else:
    print("El ph del líquid0 es neutro")