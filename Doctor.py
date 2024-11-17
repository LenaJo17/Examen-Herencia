#Clase Padre
from Persona import Persona
from Empleado import Empleado
class Doctor(Persona, Empleado):
    def __init__(self, nombre, edad, id_empleado,posicion, especialidad):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, id_empleado, "Pasante")
        self._especialidad = especialidad

    def get_especialidad(self):
        return self._especialidad

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def mostrar_informacion(self):
        return f"Doctor: {self.get_nombre()}, Edad: {self.get_edad()}, Especialidad: {self.get_especialidad()}, ID: {self.get_id_empleado()}"
