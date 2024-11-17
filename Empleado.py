#Clase Padre
class Empleado:
    def __init__(self, id_empleado, posicion):
        self._id_empleado = id_empleado
        self._posicion = posicion

    def get_id_empleado(self):
        return self._id_empleado

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def get_posicion(self):
        return self._posicion

    def set_posicion(self, posicion):
        self._posicion = posicion