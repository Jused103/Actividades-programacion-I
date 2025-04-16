# Clase estudiante

class Estudiante:
    def __init__(self):
        self.__nota = 0  

    
    def establecer_nota(self, valor):
        if 0 <= valor <= 5:
            self.__nota = valor
        else:
            print("Error: la nota debe estar entre 0 y 5.")

    
    def obtener_nota(self):
        return self.__nota


estudiante = Estudiante()


estudiante.establecer_nota(4.5)


print("La nota del estudiante es:", estudiante.obtener_nota())
