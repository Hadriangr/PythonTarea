nombre = input("Introduzca nombre completo: ")
print("Bienvenido "+ nombre + "!")

num1 = int(input("Hola " + nombre + ", introduce un número del 1 al 9: "))
if 1 <= num1 <= 9:
    num2 = int(input("Ahora introduce otro número del 1 al 9: "))
    if 1 <= num2 <= 9:
        suma = num1 + num2
        print("La suma de " + str(num1) + " y " + str(num2) + " es = " + str(suma))
    else:
        print("Número inválido, inténtelo de nuevo.")
else:
    print("Número inválido, inténtelo de nuevo.")
