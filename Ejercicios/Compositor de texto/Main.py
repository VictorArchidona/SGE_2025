import os
import random
from Graph import Graph
import string
def main():
    """
    Función principal que carga archivos de texto en un grafo y genera una "canción"
    a partir de las conexiones entre palabras.
    
    Crea un grafo con palabras de múltiples archivos de texto, y luego genera
    una secuencia de palabras basada en las conexiones del grafo.
    """

    grafo = construir_el_grafo("./Compositor de texto/Lyric de canciones")

    cancion = generar_cancion(grafo)

    print(cancion)

def construir_el_grafo(ruta_carpeta):

    grafo = Graph()

    for archivo in os.listdir(ruta_carpeta):
        if archivo.endswith(".txt"):
                with open(os.path.join(ruta_carpeta, archivo), "r", encoding="utf-8") as f:
                    texto = limpiar_texto(f.read())

                    for i in range(len(texto) - 1):
                         grafo.agregar_conexion(texto[i], texto[i + 1])

    return grafo

def limpiar_texto(texto):
    #Todo el texto lo vuelve en minusculas
    texto = texto.lower()

    #recoge todos los simbolos y los borra: "," "?" "-" ":"
    for simbolo in string.punctuation:
        texto = texto.replace(simbolo, "")

    return texto.split()

def generar_cancion(grafo, longitud = 300):
     
    nodo_actual = random.choice(grafo.node)
    resultado = [nodo_actual.content]

    for _ in range(longitud - 1):
        if not nodo_actual.edges:
            nodo_actual = random.choice(grafo.node)
            continue
          
        siguiente_arista = max(nodo_actual.edges, key = lambda a: a.weight)
        nodo_actual = siguiente_arista.destino
        resultado.append(nodo_actual.content)
    
    return " ".join(resultado)
     
if __name__ == "__main__":
    main()

