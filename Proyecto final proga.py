print("""Bienvenido, en este programa podra seleccionar y ver dependiendo de la region,comuna, los casos de una fecha en especifico que usted desee.
""")


Regiones = ["region de Arica y Parinacota", "region de Tarapacá", "region de Antofagasta", "Region de Atacama", "Región de Coquimbo", "Región de Valparaiso", "Región Metropolitana", "Región del Libertador General Bernardo O'higgins", "Región del Maule", "Región del Ñuble", "Región del Biobio", "Región de la Araucania", "Región de los Rios", "Región de los Lagos", "Región de Aysén del General Carlos Ibáñez del Campo", "Región de Magallanes"]

Codigos = ["15", "01", "02", "03", "04", "05", "13", "06", "07", "16", "08", "09", "14", "10", "11", "12"]

mensaje=input("Ingrese un mensaje: ") 

mensajep=mensaje.lower()


print("""
1 - Region de Arica y Parinacota
2 - Region de Tarapacá
3 - Region de Antofagasta
4 - Region de Atacama
5 - Region de Coquimbo
6 - Region de Valparaiso
7 - Region Metropolitana
8 - Region del Libertador General Bernardo O’Higgins
9 - Region del Maule
10 - Region del Nuble
11 - Region del Biobio
12 - Region de La Araucania
13 - Region deLos Rios
14 - Region deLos Lagos
15 - Region de Aysen
16 - Region de Magallanes y la Antartica""")


seleccion = input()
print("Su seleccion es:,"seleccion)





print("Su Region seleccionada es:,")


lalista=[] 

for i in range(lenmensaje):
    
    flag=mensajep[i]
    
    if  flag in Regiones:

        lenletra=Regiones.index(flag)

        morse=Codigos[lenletra]

        lalista.append(morse) 

        print(morse,end=" ")

print("\n",lalista)
