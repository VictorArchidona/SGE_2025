from Edge import Edge

class Node:
    def __init__(self, content):
        self.content = content
        self.edges = []
    
    def agregar_arista(self, destino):
        """Añade una arista dirigida A → B"""
        for arista in self.edges:
            if arista.destino == destino:
                arista.weight += 1
                return
        nueva_arista = Edge(destino)
        self.edges.append(nueva_arista)
    
    def obtener_vecinos(self):
        """Devuelve la lista de nodos conectados"""
        vecinos = []
        for arista in self.edges:
            vecinos.append(arista.destino)
        return vecinos
