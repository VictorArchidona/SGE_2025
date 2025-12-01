
def main():

    db = {
        "A123": {"nombre": "Ana Pérez", "asiento": "12B"},
        "B456": {"nombre": "Luis Gomez", "asiento": "14A"}
    }

    opcion = 0

    while opcion != 6:
        
        print("--MENU--")
        print("----------------------")
        print("1. Añadir Pasajero")
        print("2. Buscar Pasajero")
        print("3. Modificar Asiento")
        print("4. Eliminar Pasajero")
        print("5. Mostrar Pasajeros")
        print("6. Salir")
        print("----------------------")

        opcion = int(input("Elige una opcion: "))

        match opcion:

            case 1:

                añadir_pasajero(db)

            case 2:

                buscar_pasajeros(db)

            case 3:

                modificar_asientos(db)

            case 4:

                eliminar_pasajero(db)
                
            case 5:

                mostrar_todos(db)
            
            case 6: 
                print("Saliendo...")
                break

def añadir_pasajero(db):

    dni = str(input("Ingrese su DNI: "))
    nombre = str(input("Como se llama el pasajero: "))
    asiento = str(input("Que asiento tiene asignado: "))

    db[dni] = {"nombre": nombre, "asiento": asiento}

def buscar_pasajeros(db):

    """
    Busca pasajeros a la base de datos de pasajeros
    """

    if not db:
        print("No hay pasajeros registrados")
    else:
        for dni, valor in db.items():
            print(f"DNI: {dni} Nombre: {valor['nombre']}, Asiento {valor['asiento']}") 
            
    print("--Buscar Pasajero--")
    dni = str(input("Ingrese el dni del pasajero: "))
    
    if dni in db:
        pasajero = db[dni]
        print(f"DNI: {dni}")
        print(f"Nombre: {pasajero['nombre']}")
        print(f"Asiento: {pasajero['asiento']}")
    else:
        print("No se ha encontrado a nadie, eres un pringao")
    

def modificar_asientos(db):

    """
    Este metodo modifica el asiento del pasajero
    """
    
    if not db:
        print("No hay pasajeros")
    else:
        
        #Mostrar todos los pasajeros
        print("\n --PASAJEROS REGISTRADOS--")
        for dni, datos in db.items():
            print(f"Pasajero: {dni} nombre: {datos['nombre']} asiento: {datos['asiento']}")
        
        dni = str(input("\n Ingrese el dni del pasajero: "))
        
        if dni in db:
            
            print(f"Asiento actual {datos['asiento']} nombre del pasajero: {datos['nombre']}")
            
            asiento_nuevo = str(input("Que asiento nuevo se le ofrece al pasajero: "))
            
            #Insercion en el diccionario
            db[dni]["asiento"] = asiento_nuevo
            
            print("Asiento modificado :p")
        else:
            print(f"No se encontro el pasajero con este dni {dni}")
        
def eliminar_pasajero(db):
    
    dni = str(input("Ingrese el dni del pasajero: "))
    
    if dni in db:
        pasajero = db.pop()
        print(f"Pasajero con dni: {pasajero}, ha sido eliminado")
    else:
        print("Pasajero no encontrado")
        
def mostrar_todos(db):
    
    for dni, valor in db.items():
        print(f"Pasajero: {dni} Nombre: {valor['nombre']} Asiento: {valor['asiento']}")

if __name__ == "__main__":
    main()