# Programa que valida un pin de una cuenta de banco

pin = int(input("Inserte su número de PIN: "))

while(pin != 1234): # Va a hacer que se ejecute el loop hasta que se ejecute la condición indicada(que el pin sea 1234)
    pin = int(input("PIN incorrecto. Inserte su PIN de nuevo: "))

    if(pin == 1234):
        print("PIN aceptado.")