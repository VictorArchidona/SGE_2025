class Edge:
    """
    Clase Edge que representa una arista entre dos nodos en un grafo,
    con un peso asociado que puede incrementarse o disminuirse.
    """
    #Constructor
    def __init__(self, destino, weight):
        
        self.destino = destino
        self.weight = weight

         

    