from Edge import Edge

class Node:
    def __init__(self, content):
        self.content = content
        self.edges = []
    
    def agregar_arista(self, destino):
        """Añade una arista bidireccional A ↔ B"""
        # Añadir A → B
        existe = False
        for arista in self.edges:
            if arista.destino == destino:
                arista.weight += 1
                existe = True
                break
        if not existe:
            self.edges.append(Edge(destino))
        
        # Añadir B → A
        existe = False
        for arista in destino.edges:
            if arista.destino == self:
                arista.weight += 1
                existe = True
                break
        if not existe:
            destino.edges.append(Edge(self))
    
    def obtener_vecinos(self):
        """Devuelve la lista de nodos conectados"""
        vecinos = []
        for arista in self.edges:
            vecinos.append(arista.destino)
        return vecinos
