# Programa que dice si estás apto para subir a la montaña rusa o 

altura_min = 137
costo = 10

altura = int(input("Por favor, ingrese su altura (cm): "))
creditos = int(input("Por favor, ingrese la cantidad de créditos que posee: "))

if(altura >= altura_min and creditos >= costo):
    print("¡Disfrute su paseo!")
else:
    if(creditos >= costo and altura < altura_min):
        print("No tiene la altura suficiente como para dar un paseo.")
    elif(altura >= altura_min and creditos < costo):
        print("No tiene suficientes créditos.")
    else:
        print("Usted no cumple con ninguno de los requerimientos.")