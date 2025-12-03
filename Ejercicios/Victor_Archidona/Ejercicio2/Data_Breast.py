class Data_Breast:

    #Constructor de la clase Data_Breast, se pide el id, el diagnosis, el radius_mean y el id del hospital
    def __init__(self, id, diagnosis, radius_mean,hospital_id):
        
        self.id = id
        self.diagnosis = diagnosis  # M (maligno) o B (benigno)
        self.radius_mean = float(radius_mean)
        self.hospital_id = int(hospital_id)
    
    #Metodo string por si mostramos por terminal los valores
    def __str__(self):
        return f"ID: {self.id}, Diagnosis: {self.diagnosis}, Radius Mean: {self.radius_mean}, Hospital: {self.hospital_id}"