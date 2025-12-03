def main():
    lista_a = [0, 0, 0, 3, 7, 2, 3, 3, 3]
    lista_b = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    
    # Limitar a máximo 10 valores
    if len(lista_a) > 10:
        lista_a = lista_a[:10]  # Tomar solo primeros 10
    if len(lista_b) > 10:
        lista_b = lista_b[:10]
    
    # Las listas deben tener el mismo tamaño
    tamaño = max(len(lista_a), len(lista_b))
    lista_a = [0] * (tamaño - len(lista_a)) + lista_a  # Rellenar con ceros la lista
    lista_b = [0] * (tamaño - len(lista_b)) + lista_b
    
    suma = [0] * tamaño  # Inicializar lista de suma
    multiplicacion = tamaño
    
    print("")
    sumar(lista_a, lista_b, suma)
    print("\nResultado Suma:", suma)

    multiplicar(lista_a, lista_b, multiplicacion)
    print("Resultado Multiplicacion:", multiplicacion)
    
    
def sumar(lista_a, lista_b, suma):
    """
    Suma dos listas de dígitos posición por posición
    con el "numero" (como suma en papel)
    """
    numero = 0
    
    # Recorrer de DERECHA a IZQUIERDA (índices descendentes)
    for i in range(len(lista_a) - 1, -1, -1):
        # Sumar dígitos + numero
        total = lista_a[i] + lista_b[i] + numero
        
        # El dígito que va en esa posición es total % 10
        suma[i] = total % 10
        
        # El numero para la siguiente posición es total // 10
        numero = total // 10
    
    if numero > 0:
        print(f"Advertencia en la Suma: Desbordamiento, se perdió el dígito {numero}")

def multiplicar(lista_a, lista_b, multiplicacion):
    """
    Multiplica dos listas de dígitos posicion por posicion
    """
    
    numero = 0
    
    #Recorrer de derecha a izquierda como en el metodo sumar
    for i in range(len(lista_a) -1,  -1, -1):
        
        total = lista_a[i] * lista_b[i]
        
        multiplicacion[i] = numero % 10
        
        numero = total // 10

    if numero > 0:
        print(f"Advertencia en la Multiplicacion: Desbordamiento en la multiplicacion, se perdió el digito {numero}")
    

if __name__ == "__main__":
    main()