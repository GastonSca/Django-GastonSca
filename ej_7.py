from ej_6 import persona1


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
        if(cantidad < 0):
            self.cantidad = self.cantidad
        else:
            self.cantidad -= cantidad
        print(f"Su saldo actual es: ${self.cantidad}")

cuenta1 = Cuenta(persona1, 1500)
cuenta1.mostrar
cuenta1.ingresar(-150)
cuenta1.retirar(8000)