class BaseDeDatos:
    
    listaJugadores = {}
    
    #Constructor de la clase BaseDeDatos
    def __init__(self, nombreEquipo):
        self.nombreEquipo = nombreEquipo
        self.listaJugadores = {}
    
    #Metodo para agregar un jugador a la base de datos
    def agregarJugador(self, jugador):
        self.listaJugadores[jugador.dorsal] = jugador
    
    #Metodo para eliminar un jugador de la base de datos
    def pop(self, dorsal):
        self.listaJugadores.pop(dorsal)
        
    #Metodo para agregar un jugador a la base de datos
    def push(self, jugador):
        self.listaJugadores[jugador.dorsal] = jugador

    #Busca el jugador segun su dorsal
    def buscar(self, dorsal):

        jugador = self.listaJugadores[dorsal]

        print(f"El jugador con la dorsal {dorsal} se llama {jugador.nombre}")

    def buscarDorsal(self, dorsal):
        
        if dorsal in self.listaJugadores:
            jugador = self.listaJugadores[dorsal]
            print(f"El jugador con el dorsal {dorsal} se llama {jugador.nombre}")
        else:
            print(f"No existe jugador con dorsal {dorsal}")


    def buscarDorsalJugador(self, dorsal):
        
        if dorsal in self.listaJugadores:
            jugador = self.listaJugadores[dorsal]
            print(f"El jugador con el dorsal {dorsal} se llama {jugador.nombre}")
            return jugador
        else:
            print(f"No existe jugador con dorsal {dorsal}")
            return 
    
        
    
    def mostrarPlantilla(self):

        if not self.listaJugadores:
            print("No hay jugadores")
        else:
            for dorsal, jugador in self.listaJugadores.items():
                print(f"La dorsal {jugador.dorsal} la tiene el jugador: {jugador.nombre}")
    