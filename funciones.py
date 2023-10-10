# def suma(a,b):
#     resultado = a+b
#     return resultado


# a = input("Ingrese valor de A: ")
# if a.isnumeric(): #valida si es numerico el dato ingresado
#     b = input("Ingrese valor de B: ")
#     if b.isnumeric(): #valida si es numerico el dato ingresado
#         resultado_suma = suma(int(a), int(b)) #Convierte A y B en numeros enteros
#         print(f"La suma de A: {a} y B: {b} es = {resultado_suma}")
#     else:
#         print("Ingrese dato valido")
# else:
#     print("Ingrese dato valido")    
    
    
def palabra(a):
    return a.upper()
    
e = input("Ingrese una cadena de texto: ")
texto = palabra(e)
print(texto)

def suma_de_listas(lista):
    suma = 0  
    for numero in lista:
       suma+= numero
    return suma

mi_lista = []
while True:
    valor = input("Ingrese un valor ó escriba stop para detenerse: ")
    if valor.lower() == 'stop':
        break #Detén el bucle si el usuario ingresa ´Stop´
    # Convierte el valor ingresado a un tipo adecuado (por ejemplo, int o float) según tus necesidades
    # En este ejemplo, se asume que el usuario ingresa números enteros
    try:
        valor = int(valor)
    except ValueError:
        print("Por favor, ingrese un número valido.")
        continue
    mi_lista.append(valor)

resultado = suma_de_listas(mi_lista)
print(resultado)
        
    