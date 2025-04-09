# Ejercicio #1

class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  
        self.__edad = edad      
        self.__notas = []       

    
    def get_nombre(self):
        return self.__nombre

    
    def get_edad(self):
        return self.__edad

   
    def agregar_nota(self, nota):
        if 0 <= nota <= 10:  
            self.__notas.append(nota)
        else:
            print("⚠️ La nota debe estar entre 0 y 10.")

    
    def get_notas(self):
        return self.__notas

    
    def mostrar_info(self):
        print(f"📌 Estudiante: {self.__nombre}\nEdad: {self.__edad}\nNotas: {self.__notas}")



est1 = Estudiante("Lucho", 20)
est2 = Estudiante("Bad Bunny", 22)
est3 = Estudiante("Blessd", 19)


est1.agregar_nota(9)
est1.agregar_nota(8)

est2.agregar_nota(7)
est2.agregar_nota(10)

est3.agregar_nota(6)
est3.agregar_nota(5)


est1.mostrar_info()
est2.mostrar_info()
est3.mostrar_info()
