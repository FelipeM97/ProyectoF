print("""Bienvenido, en este programa podra seleccionar y ver dependiendo de la region,comuna, los casos de una fecha en especifico que usted desee.
""")


Regiones = ["region de Arica y Parinacota", "region de Tarapacá", "region de Antofagasta", "Region de Atacama", "Región de Coquimbo", "Región de Valparaiso", "Región Metropolitana", "Región del Libertador General Bernardo O'higgins", "Región del Maule", "Región del Ñuble", "Región del Biobio", "Región de la Araucania", "Región de los Rios", "Región de los Lagos", "Región de Aysén del General Carlos Ibáñez del Campo", "Región de Magallanes"]

Codigos = ["15", "01", "02", "03", "04", "05", "13", "06", "07", "16", "08", "09", "14", "10", "11", "12"]

mensaje=input("Ingrese un mensaje: ") # se ocupa para introducir el mensaje que se quiere traducir

mensajep=mensaje.lower() #Ocupamos el .upper pasado en clases para convertir el mensaje en mayuscula para que las letras antes declaradas coinsidan y no tenga problemas con las minisculas en su contraparte se usaria .lower

lenmensaje=len(mensajep) #Ocupamos el len para saber la longitud del mensaje

print("su traduccion respectiva es: ",end=" ") #el end ocupa para finalizar una declaración de impresión con cualquier carácter





lalista=[] 

for i in range(lenmensaje):
    
    flag=mensajep[i]
    
    if  flag in Regiones:

        lenletra=Regiones.index(flag) #se ocupa para buscar en la lista

        morse=Codigos[lenletra]

        lalista.append(morse) #combina los registros de dos o más tablas anexándolas y creando una nueva tabla. Anexar significa agregar un grupo de registros a la parte inferior de otro grupo de registros

        print(morse,end=" ")

print("\n",lalista) # la \n para que no tenga salto de linea y enviar la lista 
