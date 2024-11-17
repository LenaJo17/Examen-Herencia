#Clase Pacientes(hija)
from Persona import Persona
from Hospital import Hospital

class Paciente(Persona, Hospital):
    def __init__(self, nombre, edad, hospital_name, numero_historia, tratamiento,fecha_de_ingreso):
        Persona.__init__(self, nombre, edad)
        Hospital.__init__(self, hospital_name)
        self._numero_historia = numero_historia
        self._tratamiento = tratamiento
        self._fecha_de_ingreso = fecha_de_ingreso

    def get_numero_historia(self):
        return self._numero_historia

    def set_numero_historia(self, numero_historia):
        self._numero_historia = numero_historia

    def get_tratamiento(self):
        return self._tratamiento

    def set_tratamiento(self, tratamiento):
        self._tratamiento = tratamiento

    def get_fecha_de_ingreso(self):
        return self._fecha_de_ingreso


    def mostrar_informacion(self):
        return (f"Hospital: {self.get_name()}, Paciente: {self.get_nombre()}, Edad: {self.get_edad()}, "
                f"Historia: {self.get_numero_historia()},Tratamiento:{self.get_tratamiento()},Fecha de ingreso:{self._fecha_de_ingreso}")
