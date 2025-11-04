from Edge import Edge

class Node:
    """
    Clase Node que representa un nodo en el grafo, con un contenido asociado
    y una lista de aristas que conectan este nodo con otros.
    """
    #Constructor
    def __init__(self, content):
        """
        Inicializa un nodo con un contenido y una lista vacía de aristas.
        
        Args:
            content (str): Contenido o valor asociado al nodo.
        """
        self.content = content  # Almacena el valor o contenido del nodo
        self.edges = []  # Lista para almacenar aristas asociadas a este nodo

    """
        Busca si la arista esta creada dentro de la lista de aristas y si ya esta creada, suma uno
        al peso y si no esta creada, mete la nueva arista a la lista de aristas
    """
    #Meto
    def agregar_arista(self, destino):
        
        for arista in self.edges:
            if arista.destino == destino:
                arista.weight + 1
                return
        
        nueva_arista = Edge(destino)
        self.edges.append(nueva_arista)