
#Crea la matriz
matriz = [
    
    [1,2,3],
    [4,5,6],
    [7,8,9]

]

#Creacion de las variables
recorrido = len(matriz)
suma_principal = 0


#Recorremos la matriz en busca de la esquina arriba izquierda
for i in range(recorrido):
    suma_principal += matriz[i][i] #matriz[1][1]

#imprime el total de la suma
print(suma_principal)