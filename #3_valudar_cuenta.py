# Ejercicio #3

class Cuenta:
    def __init__(self, usuario, contraseña):
        self.__usuario = usuario          
        self.__contraseña = contraseña   

   
    def validar_acceso(self, usuario, contraseña):
        if usuario == self.__usuario and contraseña == self.__contraseña:
            print("✅ Acceso concedido. ¡Bienvenido!")
        else:
            print("❌ Acceso denegado. Usuario o contraseña incorrectos.")

   
    def cambiar_contraseña(self, contraseña_actual, nueva_contraseña):
        if contraseña_actual == self.__contraseña:
            self.__contraseña = nueva_contraseña
            print("🔒 Contraseña actualizada con éxito.")
        else:
            print("⚠️ Contraseña actual incorrecta. No se pudo actualizar.")


cuenta1 = Cuenta("usuario123", "secreto456")


cuenta1.validar_acceso("usuario123", "secreto456")  
cuenta1.validar_acceso("usuario123", "incorrecta")  
cuenta1.validar_acceso("el dios del mewing", "secreto456") 


cuenta1.cambiar_contraseña("incorrecta", "nuevaClave")  
cuenta1.cambiar_contraseña("secreto456", "nuevaClave")  


cuenta1.validar_acceso("usuario123", "nuevaClave")  
