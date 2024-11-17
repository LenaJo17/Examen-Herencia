#Clase Hija
from Doctor import Doctor
from Hospital import Hospital

class Practicante(Doctor, Hospital):
    def __init__(self, nombre, edad, hospital_name, id_empleado, posicion,especialidad, universidad,departamento_asignado, evalucacion):
        Doctor.__init__(self, nombre, edad, id_empleado,posicion, especialidad)
        Hospital.__init__(self, hospital_name)
        self._universidad = universidad
        self._departamento_asignado = departamento_asignado
        self._evalucacion = evalucacion

    def get_universidad(self):
        return self._universidad

    def set_universidad(self, universidad):
        self._universidad = universidad

    def get_departamento_asignado(self):
        return self._departamento_asignado

    def set_departamento_asignado(self, departamento_asignado):
            self._departamento_asignado = departamento_asignado

    def get_evalucacion(self):
        return self._evalucacion

    def mostrar_informacion(self):
        return (f"Hospital: {self.get_name()}, Practicante: {self.get_nombre()}, Edad: {self.get_edad()}, "
                f"ID Empleado: {self.get_id_empleado()}, Posicion:{self.get_posicion()} Especialidad: {self.get_especialidad()}, "
                f"Universidad: {self.get_universidad()},Departamento asignado:{self._departamento_asignado}, Evaluacion:{self._evalucacion}")
