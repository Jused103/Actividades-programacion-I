# Ejercicio #4

class Factura:
    IVA = 0.19 

    def __init__(self, producto, precio):
        self.__producto = producto   
        self.__precio = precio       

    
    def get_precio(self):
        return self.__precio

    
    def calcular_total(self):
        total = self.__precio * (1 + self.IVA)
        return round(total, 2)  

    
    def mostrar_factura(self):
        print(f"🛒 Producto: {self.__producto}\n💵 Precio sin IVA: ${self.__precio:.2f}\n🧾 Total con IVA: ${self.calcular_total():.2f}")


factura1 = Factura("Bugati", 120000000000)


factura1.mostrar_factura()
