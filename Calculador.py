#Este es mi código
def suma(a,b):
    dato = f"el valor de la suma entre {a} y  {b} es = {a + b}"
    return dato
def multiplicacion(c,d):
    dato = f"el valor de la multiplicación entre {c} y  {d} es = {c * d}"
    return dato
def division(e,f):
    if a != 0:
        dato = f"el valor de la división entre {e} y  {f} es = {e / f}"
        return dato
    else:
        return "Error: No se puede dividir por cero."
def resta(g,h):
    dato = f"el valor de la resta entre {g} y  {h} es = {g - h}"
    return dato


while True:
    try:
        operacion = input("Ingrese la operación (+, -, *, /) o 'salir' para finalizar: ")

        # Verificar si el usuario quiere salir
        if operacion.lower() == 'salir':
            break

        # Verificar si la operación es válida
        if operacion not in ('+', '-', '*', '/'):
            print("Operación no válida. Intente de nuevo.")
            continue

        # Obtener los operandos
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Realizar la operación correspondiente
        if operacion == '+':
            resultado = suma(num1, num2)
        elif operacion == '-':
            resultado = resta(num1, num2)
        elif operacion == '*':
            resultado = multiplicacion(num1, num2)
        elif operacion == '/':
            resultado = division(num1, num2)

        # Mostrar el resultado
        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: Ingrese números válidos.")
        
        """
#Este es el código entregado por Chatgpt optimizado
def operacion(a, b, operador): # Se aglomera en una sola función con If's anidados todas las opciones
    if operador == '+':
        resultado = a + b
    elif operador == '-':
        resultado = a - b
    elif operador == '*':
        resultado = a * b
    elif operador == '/':
        resultado = a / b    
    else:
        return "Operador no válido"
    return f"El valor de la {operador} entre {a} y {b} es = {resultado}" # se devuelve datos solicitados con respuesta

while True: #mientras se introduzcan los datos validos funcionara, de lo contrario loop 
    try:
        calculador = input("Ingresa + para sumar, - para restar, * para multiplicar y / para dividir: ")
        if calculador in ('+', '-', '*', '/'):
            a = int(input("Ingrese primer valor: "))
            b = int(input("Ingrese segundo valor: "))
            print(operacion(a, b, calculador))
        else:
            print("Ingrese una opción válida.")
        break
    except ValueError:
        print("Ingrese valores válidos.")
        """
