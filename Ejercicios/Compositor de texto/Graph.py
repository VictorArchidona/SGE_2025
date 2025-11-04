import random
from Node import Node  # Clase para representar un nodo en el grafo
from Edge import Edge  # Clase para representar una arista entre dos nodos

class Graph:
    """
    Clase Graph que representa un grafo dirigido. Permite la creación de nodos,
    la adición de aristas entre nodos, y la visualización de los nodos en el grafo.
    """
    #Constructor
    def __init__(self):
        """
        Inicializa un grafo vacío y una lista de palabras para saber si son unicas o no.
        """
        self.node = []

    """
    Devuelve el nodo segun la palabra que quieras buscar
    """
    #Metodos
    def buscar_nodo(self, palabra):

        for nodo in self.node:
            if nodo.content == palabra:
                
                return nodo

        return None
    
    """
    Este metodo mira si existe el nodo con el origen y si no existe lo crea y lo añade,
    lo mismo con el destino y agrega la conexion con ambos
    """
    #Esta creada el metodo agregar_arista en el Node porque asi con el objeto Node se puede ver el metodo
    # "Agregar_arista" :)
    def agregar_conexion(self, palabra_origen, palabra_destino):
        
        origen = self.buscar_nodo(palabra_origen)
        destino = self.buscar_nodo(palabra_destino)

        if origen is None:
            origen = Node(palabra_origen)
            self.node.append(origen)

        if destino is None:
            destino = Node(palabra_destino)
            self.node.append(destino)

        origen.agregar_arista(destino)


    