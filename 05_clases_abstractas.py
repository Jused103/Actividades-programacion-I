# Formas de pago.
from abc import ABC, abstractmethod

class metodo_de_pago(ABC):
    def __init__(self, numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso):
        self.numero_de_cuenta = numero_de_cuenta
        self.nombre_del_titular = nombre_del_titular
        self.monto = monto
        self.clave_de_acceso = clave_de_acceso

    @abstractmethod
    def mostrar_informacion(self):
        pass

# Sub clase.

class nequi(metodo_de_pago):
    def __init__(self, numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso):
        super().__init__(numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso)
    
    def mostrar_informacion(self):
        return f"nombre_del_titular : {self.nombre_del_titular}\nnumero_de_cuenta : {self.numero_de_cuenta}\nClave de acceso: {self.clave_de_acceso}\nMonto: {self.monto}"
    

class daviplata(metodo_de_pago):
    def __init__(self, numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso):
        super().__init__(numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso)
    
    def mostrar_informacion(self):
        return f"nombre_del_titular : {self.nombre_del_titular}\nnumero_de_cuenta : {self.numero_de_cuenta}\nClave de acceso: {self.clave_de_acceso}\nMonto: {self.monto}"
    

class pse(metodo_de_pago):
    def __init__(self, numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso, banco):
        super().__init__(numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso,)
        self.banco = banco
    
    def mostrar_informacion(self):
        return f"nombre_del_titular : {self.nombre_del_titular}\nnumero_de_cuenta : {self.numero_de_cuenta}\nClave de acceso: {self.clave_de_acceso}\nBanco: {self.banco}"

class targeta_de_credito(metodo_de_pago):
    def __init__(self, numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso,):
        super().__init__(numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso)   

    def mostrar_informacion(self):
        return  f"nombre_del_titular : {self.nombre_del_titular}\nnumero_de_targeta : {self.numero_de_cuenta}\nClave de acceso: {self.clave_de_acceso}"

class tergeta_de_debito(metodo_de_pago):
    def __init__(self, numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso):
        super().__init__(numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso)
    
    def mostrar_informacion(self):
        return f"nombre_del_titular : {self.nombre_del_titular}\nnumero_de_targeta : {self.numero_de_cuenta}\nClave de acceso: {self.clave_de_acceso}\n"

class efectivo(metodo_de_pago):
    def __init__(self, numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso):
        super().__init__(numero_de_cuenta, nombre_del_titular, monto, clave_de_acceso)
    
    def mostrar_informacion(self):
        return f"Monto: {self.monto}"

# isntancias.
pago_nequi = nequi("3001234567", "Juan Pérez", 50000, "1234")
pago_daviplata = daviplata("3107654321", "Ana Gómez", 75000, "5678")
pago_pse = pse("1234567890", "Carlos López", 100000, "abcd", "Banco Popular")
pago_tarjeta_credito = targeta_de_credito("9876543210", "María Torres", 200000, "4321")
pago_tarjeta_debito = tergeta_de_debito("5678901234", "Pedro Ramírez", 150000, "8765")
pago_efectivo = efectivo("", "", 50000, "")

# Mostrar información de cada método de pago
print(pago_nequi.mostrar_informacion())
print()
print(pago_daviplata.mostrar_informacion())
print()
print(pago_pse.mostrar_informacion())
print()
print(pago_tarjeta_credito.mostrar_informacion())
print()
print(pago_tarjeta_debito.mostrar_informacion())
print()
print(pago_efectivo.mostrar_informacion())