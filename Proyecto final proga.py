archivo = open("casos.txt", "r")

while True:
    linea=archivo.readline()
    if not linea:
        break
    linea=linea.strip()
    print(linea)
archivo.close()



menuprincipal = int(input("Elija una opción: \n 1- Regiones \n 2- Regiones con mayor y menor densidad de contagio \n"))




while (menuprincipal > 3):
    print("Porfavor elija una region correcta")
    menuregiones = int(input("Elija una Zona \n 1- Zona Norte \n 2- Zona Centro \n 3- Zona Sur"))
while (menuprincipal > 0):

    if menuprincipal == 1:
        print("Elija una Zona \n 1- Zona Norte \n 2- Zona Centro \n 3- Zona Sur")

        menuregiones = int(input())
            

        if menuregiones == 1:
            print("\n 1- Region de Arica y Parinacota \n 2- Region de Tarapaca \n 3- Region de Antofagasta \n 4- Region de Atacama \n 5- Region de Coquimbo \n")
        
        elif menuregiones == 2:
            print("\n 6- Region de Valparaiso \n 7- Region Metropolitana \n 8- Region del libertador Bernardo Ohiggins \n 9- Region del Maule1")
    
        elif menuregiones == 3:
            print("\n 10- Region del Ñuble \n 11- Region del Bio-Bio \n 12- Region de la Araucania \n 13- Region de los Rios \n 14- Region de los Lagos \n 15- Region de Ayse1n \n 16- Region de Magallanes y la Antartica")
    
        elif menuprincipal == 2:
            print("region 1 \n region 2 \n")       

    else :
        print("Porfavor elija una region correcta")

    menuprincipal = int(input("Elija una opción: \n 1- Regiones \n 2- Regiones con mayor y menor densidad de contagio \n"))
