print("""Bienvenido, en este programa podra seleccionar y ver dependiendo de la region,comuna, los casos de una fecha en especifico que usted desee.
""")


Regiones = ["region de Arica y Parinacota", "region de Tarapacá", "region de Antofagasta", "Region de Atacama", "Región de Coquimbo", "Región de Valparaiso", "Región Metropolitana", "Región del Libertador General Bernardo O'higgins", "Región del Maule", "Región del Ñuble", "Región del Biobio", "Región de la Araucania", "Región de los Rios", "Región de los Lagos", "Región de Aysén del General Carlos Ibáñez del Campo", "Región de Magallanes"]

Codigos = ["15", "01", "02", "03", "04", "05", "13", "06", "07", "16", "08", "09", "14", "10", "11", "12"]

mensaje=input("Ingrese un mensaje: ") 

mensajep=mensaje.lower()


menuprincipal = int(input("Elija una opción: \n 1- Regiones \n 2- Regiones con mayor y menor densidad de contagio \n"))

if menuprincipal == 1:
    print("1- Zona Norte \n 2- Zona Centro \n 3- Zona Sur")

elif menuprincipal == 2:
    print("region 1 \n region 2 \n")
else:
    print("Porfavor elija una opción correcta")

lalista=[] 

for i in range(lenmensaje):
    
    flag=mensajep[i]
    
    if  flag in Regiones:

        lenletra=Regiones.index(flag)

        morse=Codigos[lenletra]

        lalista.append(morse) 

        print(morse,end=" ")

print("\n",lalista)
