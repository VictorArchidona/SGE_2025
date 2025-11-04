class Node:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aristas = {}  # diccionario de {nodo_destino: peso}

    def agregar_arista(self, destino, peso):
        self.aristas[destino] = peso