# Programa que convierte diferentes tipos de monedas a dólares y hace una suma total

dol_pesos = 4139.50
dol_soles = 3.64
dol_reales = 5.76

cant_pesos = int(input("Ingrese la cantidad de pesos colombianos: "))
cant_soles = int(input("Ingrese la cantidad de soles peruanos: "))
cant_reales = int(input("Ingrese la cantidad de reales brazileños: "))

total_pesos = cant_pesos/dol_pesos
total_soles = cant_soles/dol_soles
total_reales = cant_reales/dol_reales

total_dolares = str(total_pesos + total_soles + total_reales)

print("La cantidad total en dólares es de " + total_dolares)