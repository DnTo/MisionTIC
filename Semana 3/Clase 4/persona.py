
class Persona:
    #init es el constructor de la clase
    def __init__(self,  documento): 
        self.documento = documento
        self.nombre = "cliente"+self.documento

