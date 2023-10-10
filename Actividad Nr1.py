def año_bisiesto(multiplo):
    if multiplo % 4 == 0:
        return f"el año {multiplo} es bisiesto" 
    else: 
        return f"el año {multiplo} no es bisiesto"

while True:
    try:
        actvidad = int(input("Ingrese año (Ej: 2023): "))
        print(año_bisiesto(actvidad))
        break  # Salir del bucle si se proporciona un valor válido
    except ValueError:
        print("Por favor, ingrese un año válido (número entero).")