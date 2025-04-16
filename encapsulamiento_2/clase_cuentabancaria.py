# Clase cuenta Bancaria

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial 

    
    def obtener_saldo(self):
        return self.__saldo

    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("El monto debe ser mayor que cero.")


cuenta = CuentaBancaria(100)


cuenta.depositar(50)

print("Saldo actual:", cuenta.obtener_saldo())
