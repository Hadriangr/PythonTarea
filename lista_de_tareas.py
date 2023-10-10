#Este fue mi codigo!
# to_do=[]# crear una lista vacia
# try: #obtener la cantidad de elementos de la lista
#         datos=int(input("Ingrese cuantos items quiere agregar a la lista: "))
# except ValueError:
#         print("Ingrese un numero valido.")
#         datos = 0  
# for i in range(datos):#agregar los elementos a la lista
#         items = input("Ingrese item de lista: ")
#         to_do.append(items)
# menu = input("Para modificar (escriba *) o eliminar (escriba -) datos? : ")
# if menu == '-': # eliminar elementos de la lista
#     eliminar = input(f"Que elemento desea eliminar de la lista {to_do} : ")
#     to_do.remove(eliminar)
# elif menu == '*': # modificar elementos de la lista
#     modificar = input(f"Que elemento desea modificar de la lista {to_do}: ")
#     to_do.remove(modificar)
#     modificar2 = input(f"Escriba la corrección del producto: ")
#     to_do.append(modificar2)
# else:
#     print(f"Ingrese valor correcto.")
# print(to_do)

#Este es el codigo de chatgpt 
def agregar_tarea(lista):
    tarea = input("Ingrese una nueva tarea: ")
    lista.append(tarea)

def eliminar_tarea(lista):
    if not lista:
        print("La lista de tareas está vacía.")
        return

    tarea = input("Ingrese la tarea que desea eliminar: ")
    if tarea in lista:
        lista.remove(tarea)
    else:
        print("La tarea no existe en la lista.")

def modificar_tarea(lista):
    if not lista:
        print("La lista de tareas está vacía.")
        return

    tarea = input("Ingrese la tarea que desea modificar: ")
    if tarea in lista:
        indice = lista.index(tarea)
        nueva_tarea = input("Ingrese la nueva descripción de la tarea: ")
        lista[indice] = nueva_tarea
    else:
        print("La tarea no existe en la lista.")

to_do = []

try:
    cantidad_elementos = int(input("Ingrese cuántas tareas quiere agregar a la lista: "))
except ValueError:
    print("Ingrese un número válido.")
    cantidad_elementos = 0

for _ in range(cantidad_elementos):
    tarea = input("Ingrese una tarea: ")
    to_do.append(tarea)

while True:
    print("\nMenu:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Modificar tarea")
    print("4. Salir")
    
    opcion = input("Elija una opción (1/2/3/4): ")
    
    if opcion == '1':
        agregar_tarea(to_do)
    elif opcion == '2':
        eliminar_tarea(to_do)
    elif opcion == '3':
        modificar_tarea(to_do)
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Intente de nuevo.")

print("Lista de tareas actualizada:", to_do)
