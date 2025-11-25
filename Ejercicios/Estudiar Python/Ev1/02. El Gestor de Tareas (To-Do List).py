def main():

    """
    Crea un programa que permita al usuario gestionar una lista de tareas pendientes.
    Las tareas no serán solo texto, sino que tendrán un estado (Pendiente/Completada).
    """    

    #Inicializacion de variables

    while True:

        tareas = {}

        print("\n --MENU DEL PROGRAMA--")

        print("1. Añadir tarea \n 2. Ver tareas \n 3. Marcar tareas como Completada \n 4. Salir")

        opcion = int(input("Ingrese una opción: "))

        match opcion:

            case 1:

                crearTarea = str(input("Que tarea quieres realizar: "))

                # hay que añadir las tareas al diccionario
                tareas

            case 2:

                print(tareas)

            case 3:



            case 4:

                
                


if __name__ == "__main__":
    main()