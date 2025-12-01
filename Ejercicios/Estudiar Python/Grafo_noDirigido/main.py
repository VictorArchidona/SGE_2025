from Grafo import Grafo

def main():
    grafo = Grafo()
    
    # Añadir aristas (conexiones bidireccionales)
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "D")
    grafo.agregar_arista("C", "D")
    
    # Imprimir grafo
    grafo.imprimir_grafo()
    
    # Obtener vecinos (ambas direcciones)
    print(f"\nVecinos de A: {[n.content for n in grafo.obtener_vecinos('A')]}")
    print(f"Vecinos de B: {[n.content for n in grafo.obtener_vecinos('B')]}")
    print(f"Vecinos de C: {[n.content for n in grafo.obtener_vecinos('C')]}")
    print(f"Vecinos de D: {[n.content for n in grafo.obtener_vecinos('D')]}")

if __name__ == "__main__":
    main()
