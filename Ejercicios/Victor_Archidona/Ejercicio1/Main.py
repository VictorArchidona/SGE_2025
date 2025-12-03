def main():

    interfaz()

#Este metodo hará de interfaz en el programa
def interfaz():
    
    
    print("--MENU EJERCICIO 1--")
    print("--------------------")
    
    #Pide el año1 por terminal
    ano1 = int(input("Ingrese el primer año: "))
    
    #El año si es 0 se repite la peticion (no existió el año 0)
    while ano1 == 0:
        ano1 = int(input("El año es 0, vuelve a ingresarlo: "))
        
    
    ano2 = int(input("Ingrese el segundo año: "))
    
    #Mientras que el año2 sea menor al año 1 o si es 0, se vuelve a pedir
    while ano2 < ano1 or ano2 == 0:
        print("El segundo año es menor al anterior")
        ano2 = int(input("Ingrese el segundo año: "))
            
    ano3 = int(input("Ingrese el tercer año: "))

    #Mientras que el año2 sea menor al año 1 o si es 0, se vuelve a pedir
    while ano3 < ano2 or ano3 == 0:
        print("El tercer año es menor al anterior")
        ano3 = int(input("Ingrese el tercer año: "))
    
    aproximado(ano1, ano2, ano3)
    
    
#Este metodo te dice cual año esta mas cerca del ano2, si ano1 o ano3
def aproximado(ano1, ano2, ano3):
    """
    Calcula qué año (ano1 o ano3) está más cerca de ano2
    Considerando que el año 0 no existió
    """
    
    # Calcular distancia entre ano1 y ano2
    if ano1 < 0 and ano2 > 0:
        # Si cruzan el año 0, restamos 1 (porque el año 0 no existe)
        distancia1 = ano2 - ano1 - 1
    else:
        distancia1 = abs(ano2 - ano1)
    
    # Calcular distancia entre ano3 y ano2
    if ano2 < 0 and ano3 > 0:
        # Si cruzan el año 0, restamos 1
        distancia3 = ano3 - ano2 - 1
    else:
        distancia3 = abs(ano3 - ano2)
    
    # Comparar distancias
    if distancia1 < distancia3:
        print(ano1)
    elif distancia3 < distancia1:
        print(ano3)
    else:
        print("EMPATE")

    
if __name__ == "__main__":
    main()