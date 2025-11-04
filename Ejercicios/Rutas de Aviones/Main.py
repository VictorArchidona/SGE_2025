import ConectorBBDD
import Graph

"""
Se pide desarrollar un sistemas capaz de generar en "tiempo real" 
la ruta más rápida y segura que tendrá que tomar un avión entre 2 ciudades.
"""

def main():

    """
    Declaracion de variables y objetos
    """
    conexionBBDD = ConectorBBDD.ConectorBBDD("127.0.0.1", "root", "password", "ciudades_db")


    #Verifica que se haya conectado a la BBDD con exito
    conexionBBDD.conexion_bbdd()
    
    interfaz(conexionBBDD)

#Hago un metodo que sea la interfaz del programa para poder reutilizarlo en otro momento
def interfaz(conexionBBDD):

    grafo = Graph.Graph(conexionBBDD)

    grafo.cargar()

    print("--Menu del Programa--")
    print("")
    print("| Lista de Ciudades para Origen y Destino |")

    ciudades_disponibles = [ciudad[1] for ciudad in conexionBBDD.mostrar_ciudades()]

    for fila in conexionBBDD.mostrar_ciudades():
        print(fila)
    print("")

    #Validacion de que el usuario ingrese una ciudad de origen valida
    while True:
        origen = input("Ingrese la ciudad de origen: ")

        if origen in ciudades_disponibles:
            break
        else:
            print("Ciudad no valida. Por favor, ingrese nuevamente.")


    #Validacion de que el usuario ingrese una ciudad de destino valida
    while True:
        destino = input("Ingrese la ciudad de destino: ")

        if destino in ciudades_disponibles:
            break
        else:
            print("Ciudad no valida. Por favor, ingrese nuevamente.")


    ciudad_Actual = origen

    while ciudad_Actual != destino:

        ruta = grafo.movimiento_dijkstra(ciudad_Actual, destino)

        if not ruta or len(ruta) < 2:
            print("No se encontró una ruta disponible desde", ciudad_Actual, "hasta", destino)
            return

        siguiente = ruta[1]
        print(f"viajando de {ciudad_Actual} a {siguiente}...")

        input("Presiona Enter para continuar el vuelo...")

        grafo.actualizar_peso(ciudad_Actual, siguiente)

        ciudad_Actual = siguiente

    if(ciudad_Actual == destino):
        print(f"¡Has llegado a tu destino: {destino}!")

if __name__ == "__main__":
    main()