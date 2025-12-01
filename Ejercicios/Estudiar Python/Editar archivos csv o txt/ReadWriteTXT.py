import os

archivo_origen = 'archivo.txt'
archivo_temporal = 'temporal.txt'

#Verificamos si existe (para evitar errores)
if not os.path.isfile(archivo_origen):
    with open(archivo_origen, 'w') as f:
        f.write("Línea 1\nLínea 2\nLínea 3\n")
    
with open(archivo_origen, 'r') as origen, open(archivo_temporal, 'w') as temporal:
    for linea in origen:
        
        #Reemplazar Linea 1 por Primera Línea
        nueva_linea = linea.replace('Linea 1', 'Primera Linea')

        #Ejemplo: convertir todo a mayusculas
        # nueva_linea = nueva_linea.upper()

        temporal.write(nueva_linea)

#2. Reemplazo final
os.remove(archivo_origen)  # Eliminar el archivo original
os.rename(archivo_temporal, archivo_origen)  # Renombrar el archivo temporal