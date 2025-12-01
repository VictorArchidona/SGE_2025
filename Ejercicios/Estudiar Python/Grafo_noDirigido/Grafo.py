from Node import Node

class Grafo:
    def __init__(self):
        self.nodos = []
    
    def agregar_nodo(self, content):
        """Añade un nodo al grafo si no existe"""
        for nodo in self.nodos:
            if nodo.content == content:
                return nodo
        nuevo_nodo = Node(content)
        self.nodos.append(nuevo_nodo)
        return nuevo_nodo
    
    def agregar_arista(self, origen_content, destino_content):
        """Crea una conexión bidireccional origen ↔ destino"""
        nodo_origen = self.agregar_nodo(origen_content)
        nodo_destino = self.agregar_nodo(destino_content)
        nodo_origen.agregar_arista(nodo_destino)
    
    def obtener_vecinos(self, content):
        """Devuelve los vecinos de un nodo"""
        for nodo in self.nodos:
            if nodo.content == content:
                return nodo.obtener_vecinos()
        return []
    
    def imprimir_grafo(self):
        """Muestra la estructura del grafo"""
        print("\n=== GRAFO NO DIRIGIDO ===")
        for nodo in self.nodos:
            vecinos = [v.content for v in nodo.obtener_vecinos()]
            print(f"{nodo.content} ↔ {vecinos}")
