# Clase inventario. 
#5. Diseña una clase Inventario con un atributo privado cantidad. Implementa métodos para agregar y retirar unidades, asegurándote de que no se retiren más unidades de las disponibles. También crea un método para consultar la cantidad actual.

class Inventario:
    def __init__(self, cantidad):
        self.__cantidad = 0
    
    def agregar(self, unidades):
        if unidades > 0:
            self.__cantidad += unidades
        else:
            print("Error: las unidades a agregar deben ser mayores que cero.")

    
    def retirar(self, unidades):
        if unidades > self.__cantidad:
            print("Error: no hay suficientes unidades en el inventario.")
        elif unidades <= 0:
            print("Error: las unidades a retirar deben ser mayores que cero.")
        else:
            self.__cantidad -= unidades

    
    def consultar(self):
        return self.__cantidad


inventario1 = Inventario()
inventario1.agregar(100)
inventario1.retirar(30)
print("Cantidad actual en inventario:", inventario1.consultar())
        