def main():

    archivo = 'datos.csv'

    #1. Leer todo el contenido en una lista de lineas
    with open(archivo, 'r', encoding='utf-8') as f:

        lineas = f.readlines()

        nuevas_lineas = []
        cabecera = lineas[0]
        nuevas_lineas.append(cabecera) #Guardamos la cabecera sin cambios

        #Procesar cada linea despues de la cabecera
        for linea in lineas[1:]:
            linea = linea.strip() #Eliminar espacios en blanco y saltos de linea
            if not linea: continue #Saltar lineas vacias

            #Separamos por comas para obtener una lista
            campos = linea.split(',')

            #Supongamos que: col 0 es Nombre, col 1 es Edad
            nombre = campos[0]
            edad = int(campos[1])

            #Modificar la edad (por ejemplo, sumar 1)
            edad += 1

            #Actualizamos la linea modificada
            campos[1] = str(edad)

            #Volvemos a unir con comas y agregamos el salto de linea
            nueva_linea = ','.join(campos) + '\n'
            nuevas_lineas.append(nueva_linea)

    #2. Escribir las lineas modificadas de vuelta al archivo
    with open(archivo, 'w', encoding='utf-8') as f:
        f.writelines(nuevas_lineas)

if __name__ == "__main__":
    main()