# Clase paciente.

class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__historial_medico = []

    
    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def establecer_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("Error: la edad debe ser un número positivo.")

    def agregar_diagnostico(self, diagnostico):
        self.__historial_medico.append(diagnostico)

    
    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def obtener_historial(self):
        return self.__historial_medico


paciente1 = Paciente()
paciente1.establecer_nombre("Carlos")
paciente1.establecer_edad(45)
paciente1.agregar_diagnostico("Hipertensión")
paciente1.agregar_diagnostico("Diabetes tipo 2")

print("Nombre:", paciente1.obtener_nombre())
print("Edad:", paciente1.obtener_edad())
print("Historial Médico:", paciente1.obtener_historial())
