#Clase hija
from Persona import Persona
from Hospital import Hospital

class Visita(Persona, Hospital):
    def __init__(self, nombre, edad, hospital_name, motivo_visita, hora_de_entrada):
        Persona.__init__(self, nombre, edad)
        Hospital.__init__(self, hospital_name)
        self._motivo_visita = motivo_visita
        self._hora_de_entrada = hora_de_entrada



    def get_motivo_visita(self):
        return self._motivo_visita

    def set_motivo_visita(self, motivo_visita):
        self._motivo_visita = motivo_visita

    def get_hora_de_entrada(self):
        return self._hora_de_entrada

    def set_hora_de_entrada(self, hora_de_entrada):
        self._hora_de_entrada = hora_de_entrada


    def mostrar_informacion(self):
        return (f"Hospital: {self.get_name()}, Visita: {self.get_nombre()}, Edad: {self.get_edad()}, "
                f"Motivo: {self.get_motivo_visita()}"
                f"hora_de_entrada:{self.get_hora_de_entrada()}")
