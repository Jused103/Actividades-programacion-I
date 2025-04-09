# Ejercicio 2   

class Pago:
    def __init__(self, nombre, tarjeta, monto):
        self.__nombre = nombre      
        self.__tarjeta = tarjeta    
        self.__monto = monto        
        self.__estado = "Pendiente" 

    
    def get_estado(self):
        return self.__estado

    
    def procesar_pago(self):
        if self.__monto > 0:
            self.__estado = "Pagado ✅"
            print("💳 Pago procesado con éxito.")
        else:
            self.__estado = "Error ❌"
            print("⚠️ Monto inválido. No se puede procesar el pago.")

    
    def mostrar_info(self):
        tarjeta_oculta = "**** **** **** " + self.__tarjeta[-4:]  
        print(f"📌 Cliente: {self.__nombre}\nTarjeta: {tarjeta_oculta}\nMonto: ${self.__monto}\nEstado: {self.__estado}")


pago1 = Pago("Pablo londra!!", "1234567812345678", 100)


pago1.mostrar_info()


pago1.procesar_pago()


pago1.mostrar_info()
