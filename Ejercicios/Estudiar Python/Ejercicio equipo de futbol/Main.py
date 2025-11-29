from Jugador import Jugador
from BaseDeDatos import BaseDeDatos

def main():

    interfaz()

def interfaz():

    equipo = BaseDeDatos("Barcelona")

    while True:
        print("Bienvenido al sistema de gestión del equipo de fútbol")
        print("1. Agregar jugador")
        print("2. Mostrar jugadores")
        print("3. Buscar Jugadores")
        print("4. Eliminar Jugador")
        print("5. Salir")
            
        opcion = int(input("Selecciona una opcion: "))
            
        match opcion:
                
            case 1:

                nombre = str(input("Como se llama el jugador: "))

                posicion = str(input("En que posicion juega: "))

                dorsal = int(input("Que dorsal tiene el jugador: "))

                jugador = Jugador(nombre, posicion, dorsal)

                equipo.push(jugador)
            case 2:
                equipo.mostrarPlantilla()
                
            case 3:

                dorsal = int(input("Que dorsal tiene el jugador: "))

                equipo.buscarDorsal(dorsal)
                
                
            case 4:

                dorsal = int(input("Que dorsal tiene el jugador que quieres eliminar"))

                jugador = equipo.buscarDorsalJugador(dorsal)

                equipo.pop(jugador.dorsal)


if __name__ == "__main__":
    main()