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
