class Tripleta:
    
    #Constructor de la clase Tripleta, se pide el id del hospital, el minimo y el maximo
    def __init__(self, id_hospital, min_value, max_value):
        self.hospital_id = int(id_hospital)
        self.min = float(min_value)
        self.max = float(max_value)
    
    def __str__(self):
        return f"Hospital {self.hospital_id}: Min={self.min}, Max={self.max}"