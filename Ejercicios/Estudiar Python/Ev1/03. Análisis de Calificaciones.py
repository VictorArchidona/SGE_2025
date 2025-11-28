def main():

    lista_ejemplo = [85, 62, 90, 78, 55, 95, 70, 68]

    interfaz(lista_ejemplo)
    
def interfaz(lista_ejemplo):

    while True:
        
        print("--MENU CALIFICACIONES--")
        print("")
        print("----------------------------------")
        print("Opcion 1: Promedio Calificaciones")
        print("Opcion 2: Calificacion Maxima")
        print("Opcion 3: Calificacion Minima")
        print("Opcion 4: Alumnos Aprobados")
        print("----------------------------------")
        print("Para salir ingrese otro numero o palabra...")

        opcion = int(input("Ingrese una opcion: "))

        match opcion:

            case 1:
                promedio_calf(lista_ejemplo)
            case 2:
                calificacion_max(lista_ejemplo)
            case 3:
                calificacion_min(lista_ejemplo)
            case 4:
                calificacion_aprob(lista_ejemplo)
            case _:
                print("Opcion no valida, saliendo del programa...")
                break


def promedio_calf(lista_ejemplo):


    suma = 0

    for i in lista_ejemplo:
        suma = i + suma
                
    suma = suma / len(lista_ejemplo)

    print("")
    print(f"promedio: {suma}")
    print("")

def calificacion_max(lista_ejemplo):

    calificacion = max(lista_ejemplo)

    print("")
    print(calificacion)
    print("")

def calificacion_min(lista_ejemplo):

    calificacion = min(lista_ejemplo)

    print("")
    print(calificacion)
    print("")

def calificacion_aprob(lista_ejemplo):

    contador = 1

    for i in lista_ejemplo:

        if i >= 70:
            calificacion = "Aprobado"
        else:
            calificacion = "Suspendido"
        
        print(f"El alumno {contador} ha {calificacion}")
        contador = contador + 1

    print("")

        
if __name__ == "__main__":
    main()