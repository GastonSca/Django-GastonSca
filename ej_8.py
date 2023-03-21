from ej_6 import Persona

class Cuenta:
    def __init__(self, titular=None, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
    
    @property
    def get_titular(self):
        return self.titular

    
    def set_titular(self, persona):
        self.titular = persona

    @property
    def get_cantidad(self):
        return self.cantidad

    
    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
    
    @property
    def mostrar(self):
        print(f"Nombre: {self.titular.nombre}\nEdad: {self.titular.edad}\nDNI: {self.titular.dni}\nSaldo: {self.cantidad}")
    
    
    def ingresar(self, monto_ingreso):
        if(monto_ingreso < 0):
            self.cantidad = self.cantidad
        else:
            self.cantidad = self.cantidad + monto_ingreso
        print(f"Su saldo actual es: ${self.cantidad}")
        
    def retirar(self, cantidad=0):
        print(f"Saldo anterior: ${self.cantidad}")
        if(cantidad < 0):
            self.cantidad = self.cantidad
        else:
            self.cantidad -= cantidad
        print(f"Monto a retirar: (${cantidad})")
        print(f"Saldo actual: ${self.cantidad}")

class CuentaJoven(Cuenta):

    def __init__(self, titular=None, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    @property
    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, nueva_bonificacion):
        self.bonificacion = nueva_bonificacion
    
    def es_titular_valido(self):
        return self.titular.edad > 18 and self.titular.edad < 25
    
    
    def retirar(self, cantidad=0):
        if self.es_titular_valido():
            return super().retirar(cantidad)
        else:
            print("El titular de la cuenta no tiene autorización para realizar un retiro.")
    
        
        

p2 = Persona("Daniel", 26, 39451265)
cj1 = CuentaJoven(p2, 12500, 25)
cj1.retirar(500)
