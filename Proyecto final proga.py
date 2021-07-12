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
        
 #en esta seccion se despliegan las regiones con sus respectivos codigos dependiendo de la eleccion del usuario
        print("""
    1 - Region de Arica y Parinacota, el respectivo Codigo es = 15

    2 - Region de Tarapacá, el respectivo Codigo es = 01

    3 - Region de Antofagasta, el respectivo Codigo es = 02

    4 - Region de Atacama, el respectivo Codigo es = 03

    5 - Region de Coquimbo, el respectivo Codigo es = 04

    6 - Region de Valparaiso, el respectivo Codigo es = 05

    7 - Region Metropolitana, el respectivo Codigo es = 13

    8 - Region del Libertador General Bernardo O’Higgins, el respectivo Codigo es = 06

    9 - Region del Maule, el respectivo Codigo es = 07

    10 - Region del Nuble, el respectivo Codigo es = 16

    11 - Region del Biobio, el respectivo Codigo es = 08

    12 - Region de La Araucania, el respectivo Codigo es = 09

    13 - Region deLos Rios, el respectivo Codigo es = 14

    14 - Region deLos Lagos, el respectivo Codigo es = 10

    15 - Region de Aysen, el respectivo Codigo es = 11

    16 - Region de Magallanes y la Antartica, el respectivo Codigo es = 12""")
        print("Ejecute el programa nuevamente para elegir otras opciones")
        break
#En esta sección de codigo el usuario al elegiir el numero 3 se despliega un grafico de barra con la region con mayor contagios, y la region con menos contagios
    elif MenuPrincipal == 3:

        eje_x = ["Metropolitana", "Aysen"]

        eje_y = [1444791,19290 ]

        plt.bar(eje_x, eje_y)

        plt.ylabel("Contagios")

        plt.xlabel("Regiones")

        plt.title("Region con mayor y menor cantidad de contagios")

        plt.show()

        break
#al elegir el numero 4 el programa finaliza
    elif MenuPrincipal == 4:
        print("Programa finalizado")
        break
