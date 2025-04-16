# Clase persona. #1

class persona:
    def __init__(self, nombre, edad ):
        self.__nombre = nombre
        self.__edad = edad
        
    def mostrar_info(self):
        print (f"Nombre: {self.__nombre}")
        print (f"Edad: {self.__edad}")


# objeto.
persona_1 = persona("bad bunny", 25)

persona_1.mostrar_info()
