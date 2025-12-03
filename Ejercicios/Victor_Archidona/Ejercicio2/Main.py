from Data_Breast import Data_Breast
from Tripleta import Tripleta
import csv

def main():
    # Leer datos del CSV
    datos = leer_csv()
    
    # Obtener tripletas
    tripletas = min_max_radius_mean(datos)
    
    # Mostrar resultados
    print("Resultados por hospital (diagnósticos malignos):")
    for tripleta in tripletas:
        print(tripleta)


def leer_csv():
    """
    Lee el archivo CSV y devuelve una lista de objetos Data_Breast
    """
    lista_datos = []
    
    archivo = 'data.csv'
    
    with open(archivo, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        
        for row in csv_reader:
            # Crear objeto Data_Breast con los campos que se piden (id del hospital y el radius)
            dato = Data_Breast(row.id_hospital, row.radius_mean)
            lista_datos.append(dato)
    
    return lista_datos

def min_max_radius_mean(list):
    """
    Devuelve una lista de tripletas con minimo y maximo de radius_mean 
    para diagnósticos malignos (M) por cada hospital
    """
    # Diccionario para agrupar por id del hospital
    hospitales = {}
    
    # Filtrar solo los diagnósticos malignos y agrupar por hospital
    for dato in list:
        if dato.diagnosis == 'M':  # Solo malignos
            hospital = dato.hospital_id
            
            if hospital not in hospitales:
                hospitales[hospital] = []
            
            hospitales[hospital].append(dato.radius_mean)
    
    # Calcular minimo y maximo para cada hospital
    resultado = []
    for id_hospital, valores in hospitales.items():
        min_value = min(valores)
        max_value = max(valores)
        tripleta = Tripleta(id_hospital, min_value, max_value)
        resultado.append(tripleta)
    
    return resultado

if __name__ == "__main__":
    main()