# Ejercicio #5

class MenuOpciones:
    def __init__(self):
        self.__opcion = None  
        self.__opciones_validas = {1: "Iniciar", 2: "Configurar", 3: "Salir"}  # Opciones permitidas

    
    def set_opcion(self, nueva_opcion):
        if nueva_opcion in self.__opciones_validas:
            self.__opcion = nueva_opcion
            print(f"✅ Opción cambiada a: {self.__opciones_validas[nueva_opcion]}")
        else:
            print("⚠️ Opción inválida. Elige 1, 2 o 3.")

    
    def get_opcion(self):
        return self.__opcion

    
    def ejecutar_accion(self):
        if self.__opcion == 1:
            print("🚀 Iniciando el sistema...")
        elif self.__opcion == 2:
            print("⚙️ Abriendo configuración...")
        elif self.__opcion == 3:
            print("👋 Saliendo del programa...")
        else:
            print("❌ No hay opción seleccionada.")


menu = MenuOpciones()


menu.set_opcion(1) 
menu.ejecutar_accion()  

menu.set_opcion(2)  
menu.ejecutar_accion()  

menu.set_opcion(5)  
menu.ejecutar_accion()  

menu.set_opcion(3)  
menu.ejecutar_accion() 
