import random
from Node import Node  # Clase para representar un nodo en el grafo
from Edge import Edge  # Clase paraº representar una arista entre dos nodos

class Graph:
    """
    Clase Graph que representa un grafo dirigido. Permite la creación de nodos,
    la adición de aristas entre nodos, y la visualización de los nodos en el grafo.
    """

    #Constructor
    def __init__(self, db):
        """
        Inicializa un grafo vacío 
        """
        self.db = db
        self.node = {}  # Lista para almacenar los nodos del grafo
    
    """
    Carga los nodos de la base de datos al grafo y las aristas de la bbdd
    """
    #Metodos
    def cargar(self):
        """
        Carga los nodos y aristas desde la base de datos al grafo
        """
        # Obtener diccionario de ciudades {id: nombre}
        ciudades = {c[0]: c[1] for c in self.db.mostrar_ciudades()}
        
        # Obtener enlaces
        enlaces = self.db.mostrar_enlaces()

        # Crear nodos para cada ciudad
        for _, nombre in ciudades.items():
            self.node[nombre] = Node(nombre)

        # Crear aristas entre nodos
        for enlace in enlaces:
            try:
                # Obtener IDs y nombres de ciudades
                origen_id = enlace[1]
                destino_id = enlace[2]
                origen_nombre = ciudades[origen_id]
                destino_nombre = ciudades[destino_id]

                # Obtener valores de los atributos con manejo de errores
                saturacion = float(enlace[3]) if enlace[3] is not None else 0.0
                tiempo = float(enlace[4]) if enlace[4] is not None else 0.0
                animales = bool(enlace[5]) if enlace[5] is not None else False

                # Calcular peso
                peso = self.calcular_peso(saturacion, tiempo, animales)

                # Agregar aristas en ambas direcciones
                self.node[origen_nombre].agregar_arista(self.node[destino_nombre], peso)
                self.node[destino_nombre].agregar_arista(self.node[origen_nombre], peso)

            except (KeyError, IndexError, ValueError) as e:
                print(f"Error procesando enlace {enlace}: {str(e)}") 
    
    def calcular_peso(self, saturacion_transito, tiempo_ruta, ruta_animales):
    
        peso_saturacion = float(saturacion_transito) * 0.6
        peso_tiempo = tiempo_ruta * 0.4
        bonus_animales = 30 if bool(ruta_animales) else 0

        total = peso_saturacion + peso_tiempo + bonus_animales
        return total


    def actualizar_peso(self, origen, destino):
        
        saturacion = round(random.uniform(0.0, 1.0), 2)
        tiempo = random.randint(30, 90)
        animales = random.choice([True, False])

        peso = self.calcular_peso(saturacion, tiempo, animales)

        nodo_origen = self.node[origen]
        nodo_destino = self.node[destino]
        nodo_origen.aristas[nodo_destino] = peso
        nodo_destino.aristas[nodo_origen] = peso

        # Mostrar condiciones actualizadas
        print(f"Condiciones entre {origen} y {destino} actualizadas:")
        print(f"Saturación: {saturacion}, Tiempo: {tiempo} min, Animales: {animales}")
        print(f"Nuevo peso: {peso:.2f}")

    def movimiento_dijkstra(self, inicio, fin):
        """
        Implementa el algoritmo de Dijkstra para encontrar la ruta más corta
        """
        if inicio not in self.node or fin not in self.node:
            print("Uno o ambos nodos no existen en el grafo.")
            return None

        # Inicialización
        distancias = {nodo: float('inf') for nodo in self.node.values()}
        distancias[self.node[inicio]] = 0
        anterior = {}
        no_visitados = set(self.node.values())

        while no_visitados:
            # Encontrar el nodo no visitado con menor distancia
            actual = min(no_visitados, key=lambda nodo: distancias[nodo])
            no_visitados.remove(actual)

            # Si llegamos al destino, construir y devolver el camino
            if actual.nombre == fin:
                camino = []
                while actual.nombre != inicio:
                    camino.insert(0, actual.nombre)
                    actual = anterior[actual]
                camino.insert(0, inicio)
                return camino

            # Actualizar distancias a los vecinos
            for vecino, peso in actual.aristas.items():
                if vecino in no_visitados:
                    nueva_distancia = distancias[actual] + peso
                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        anterior[vecino] = actual

        print("No hay ruta disponible entre las ciudades.")
        return None

    def obtener_nodo(self):

        return self.node