import mysql.connector

class ConectorBBDD:
    def __init__(self, host, user, password, database):

        self.conexion = mysql.connector.connect( 
            
            host = host,
            user = user,
            password = password,
            database = database,
            port = 3307 #Puerto del MYSQL Workbench
        )
        self.cursor = self.conexion.cursor()
        self.conexion_bbdd()    

    def conexion_bbdd(self):
        
        if self.conexion.is_connected():    

            print("Conexion exitosa con el MySQL")
            print("------------------------------")

    def mostrar_ciudades(self):
        self.cursor.execute("SELECT id_ciudad, nombre FROM ciudades")
        return self.cursor.fetchall()


    def mostrar_enlaces(self):

        query = "SELECT * FROM enlaces"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        return resultados

    def cerrar(self):
        
        self.conexion.close()
        self.cursor.close()