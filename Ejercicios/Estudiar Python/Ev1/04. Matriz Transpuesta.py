
matriz = [
    
    [1, 2],
    [4, 5],
    [7, 8]
]

# Obtener el numero de filas y columnas originales
columnas_originales = len(matriz[0])
filas_originales = len(matriz)

# Crear una nueva matriz transpuesta
transpuesta = []

#Crea las celdas en la matriz transpuesta
for i in range(columnas_originales):
    
    nuevas_filas = []
    transpuesta.append(nuevas_filas)

#Rellenar las celdas vacias con los valores de la matriz
for i in range(filas_originales):
    for j in range(columnas_originales):
        
        valores = matriz[i][j]
        
        transpuesta[j].append(valores)

print(matriz)
print(transpuesta)