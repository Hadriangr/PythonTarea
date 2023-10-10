
def area_rectangulo(base, altura):
    area = base*altura
    return area
def area_circulo(a): 
    radio = (a**2) * 3.14159
    return radio
def relacion(num1,num2):
    if num1 > num2:
        a= print('1')
        return a
    elif num1 < num2:
       a = print('-1')
       return a
    elif num1 == num2:
       a=print('0')
       return a
    else:
       print("Ha ocurrido un error.")      
def intermedio(a,b):
    medio = (a+b) / 2
    return medio
def recortar(a, b, c):
    if a < b:
        return f"Limite inferior {b}"
    elif a > c:
        return f"Limite superior {c}"
    elif b <= a <= c:
        return f"Valor entre los límites {a}"
    else:
        return "Ocurrió un error."

        

while True:
        print("\n Menu")
        print("1- Calcular Area de un rectangulo.")
        print("2- Calcular area de un circulo.") 
        print("3- Relacion.")
        print("4- Intermedio")
        print("5- Recortar") 
        print("6- placeholder")
        print("7- Salir")
       
        opcion = input("Elija una opción (1/2/3/4/5/6/7): ") 
        if opcion == '1':
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            print(area_rectangulo(base,altura))
        elif opcion == '2':
            a = float(input("Ingrese el radio del circulo para calcular su area: "))
            print(area_circulo(a))
        elif opcion == '3':
            num1 = int(input("Ingrese valor 1: "))
            num2 = int(input("Ingrese valor 2: "))
            print(relacion(num1,num2))
        elif opcion == '4':
            a = float(input("Ingrese valor 1: "))
            b = float(input("Ingrese valor 2: "))
            print(intermedio(a,b))
        elif opcion == '5':
            a = int(input("Ingrese valor: "))
            b = int(input("Ingrese límite inferior: "))
            c = int(input("Ingrese límite superior: "))  
            resultado = recortar(a, b, c)
            print(resultado)

        elif opcion == '6':
            print("hola mundo")
        else:
            print("Error")
            break   

    