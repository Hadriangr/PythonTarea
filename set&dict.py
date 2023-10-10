"""paises = {"inglaterra","USA","Mexico"}
paises.update(["Italia","Islandia","Argentina","Portugal","USA"])
paises.remove("Italia")
paises.discard("Chile")
print(paises)"""

dict2 ={}
nombre = input(str("Ingrese su Nombre: "))
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su direccion: ")

dict2["nombre"] = nombre
dict2["edad"] = edad
dict2["direccion"] = direccion


print(f"{nombre} tienes {edad} y vives en {direccion}")