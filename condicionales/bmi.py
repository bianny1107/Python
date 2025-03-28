# Programa que calcula el BMI

masa = float(input("Inserte su masa (kg): "))
altura = float(input("Inserte su altura (m): "))

total_altura = altura ** 2
bmi = masa/total_altura

if(bmi <= 18.5):
    print("Su peso está por debajo de lo indicado.")
elif(bmi >= 18.5 and bmi <= 24.9):
    print("Su peso es normal.")
elif(bmi >= 25 and bmi <= 29.9):
    print("Usted tiene sobrepeso.")
else:
    print("Usted tiene obesidad.")

    if(bmi >= 30 and bmi <= 34.9):
        print("Su obesidad es de grado 1 (moderada).")
    elif(bmi >= 35 and bmi <= 39.9):
        print("Su obesidad es de grado 2 (severa).")
    else:
        print("Su obesidad es de grado 3 (mórbida).")