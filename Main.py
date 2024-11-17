from Paciente import Paciente
from Visita import Visita
from Practicante import Practicante


def main():
    # Crear instancia de Paciente
    paciente = Paciente(nombre="Analissa Pérez", edad=33, hospital_name="Hospital Central", numero_historia="H1234",tratamiento="Quimioterapia",fecha_de_ingreso="24 de mayo 2024")
    print(paciente.mostrar_informacion())
    print("-" * 50)

    # Crear instancia de Visita
    visita = Visita(nombre="Juan López", edad=50, hospital_name="Hospital Central", motivo_visita="Consulta familiar", hora_de_entrada="19:15")
    print(visita.mostrar_informacion())
    print("-"*50)

    # Crear instancia de Practicante
    practicante = Practicante(nombre="Mohacid Gómez", edad=25, hospital_name="Hospital Central", id_empleado="P002", posicion="Pasante", especialidad="Pediatria", universidad="Tecnologico de Zacatepec", departamento_asignado="Oncologia", evalucacion="si aplica")
    print(practicante.mostrar_informacion())
    print("-" * 50)

if __name__ == "__main__":
    main()