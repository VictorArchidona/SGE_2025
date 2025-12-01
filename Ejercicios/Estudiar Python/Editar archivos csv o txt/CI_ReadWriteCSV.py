import csv
import os

def main():


    archivo_origen = 'datos.csv'
    archivo_temporal = 'temp.csv'

    #1. Abrimos los archivos para LEER y ESCRIBIR 
    with open(archivo_origen, 'r', encoding='utf-8') as f_in, \
        open (archivo_temporal, 'w', encoding='utf-8') as f_out:

        reader = csv.DirectReader(f_in)
        #Copiamos los nombres de las columnas del original
        campos = reader.fieldnames

        writer = csv.DictWriter(f_out, fieldnames=campos)
        writer.writeheader()

        #2. Procesamos fila por fila
        for fila in reader:
            #--LOGICA AQUI--
            #Ejemplo: Convertir la columna 'Nombre' a mayusculas
            fila['Nombre'] = fila['Nombre'].upper()

            #Ejemplo: sumar 5 al 'stock'
            stock_actual = int(fila['Stock'])
            fila['Stock'] = stock_actual + 5

            #Escribimos la fila modificada en el archivo temporal
            writer.writerow(fila)
        
    #3. Reemplazamos el archivo original con el temporal
    os.remove(archivo_origen)
    os.rename(archivo_temporal, archivo_origen)

if __name__ == "__main__":
    main()