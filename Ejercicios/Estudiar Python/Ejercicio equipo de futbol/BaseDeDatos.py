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
    def pop(self, jugador):
        self.listaJugadores.pop(jugador.dorsal)
        
    #Metodo para agregar un jugador a la base de datos
    def push(self, jugador):
        self.listaJugadores[jugador.dorsal] = jugador