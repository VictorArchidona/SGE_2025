class Jugador:
    
    #Constructor de la clase Jugador
    def __init__(self, nombre, posicion, dorsal, goles = 0):
        self.nombre = nombre
        self.posicion = posicion
        self.dorsal = dorsal
        self.goles = goles

    #Metodo para representar al jugador como cadena de texto
    def __str__(self):
        return f"Jugador: {self.nombre}, Posición: {self.posicion}, Número: {self.dorsal}, Goles: {self.goles}"
    
    
    #Getters y Setters 
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor.strip()
        
    @property
    def posicion(self):
        return self._posicion
    
    @posicion.setter
    def posicion(self, valor):
        self._posicion = valor

