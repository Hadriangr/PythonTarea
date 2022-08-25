# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:07:23 2022
Escribe un programa en la consola de python que pida al usuario su peso (en kg)
 y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable
 , e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa
 corporal calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en
 una carpeta comprimida zip.
@author: hadri
"""
import math
 
peso = float(input("Ingrese su peso en Kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))
 
IMC = round(peso/math.pow(estatura,2),1)
 
print("Su IMC es de "+str(IMC)) 