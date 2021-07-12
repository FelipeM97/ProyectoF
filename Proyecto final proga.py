#Felipe Andres Mendez Bravo 21064358-3 Seccion 1  
#Ariel Andres Marió Muñoz 21173102-8 Seccion 1

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#importamos las librerias correspondientes como pandas y numpy para la manipulacion de data y el matplot para el uso de graficos
#importante igual tener instaladas las librerias para el funcionamiento del mismo

#se ocupa para leer data
data = pd.read_csv("CasosActivosPorComuna.csv", index_col=1 )
#Se linkea con el archivo .csv que tenemos



#se crea un dataframe
guardado = pd.DataFrame(data)

#ocupamos esta funcion para obtener "comuna" y almacenarlas en una variable
comunas = []
for i in guardado["Comuna"]:
    if i =="Total":
        continue
    else:
        comunas.append(i)
#En esta seccion se mostrara el menu para poder elegir lo que deseamos hacer
print("\nColoque el numero 1 para poder ver las comunas \nColoque el numero 2 si desea ver la regiones\nColoque el numero 3 si desea ver la region con mayor y menor cantidad de contagios\nColoque el numero 4 para finalizar el programa")

#Aca el codigo entra en un ciclo while para que el usuario se le repita en caso de elegir una opcion que no se encuentra dentro del menu
MenuPrincipal = int(input(""))
while (MenuPrincipal > 3):
    print("Porfavor elija una opcion correcta")
    MenuPrincipal = int(input("\nColoque el numero 1 para poder ver las comunas \nColoque el numero 2 si desea ver la regiones\nColoque el numero 3 si desea ver la region con mayor y menor cantidad de contagios\nColoque el numero 4 para finalizar el programa"))
while (MenuPrincipal > 0):


    if MenuPrincipal == 1:
        
        aray = np.column_stack((comunas, ))
        #se ocupa el column_stack para agrupar las comunas en una columna
        areas = {"comunas":comunas}
        print(aray,end=", ")

        print("\n\n escoja la comuna que desea escribiendola tal cual asi se muestra: ")
        eleccion = input()
        break

    elif MenuPrincipal == 2:
