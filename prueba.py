class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # getters y setters para Nombre:
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

    # getters y setters para Edad:
    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo")

    # getters y setters para DNI:
    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9 and dni.isnumeric():
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de texto de 9 dígitos numéricos")

    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._dni}")

    def es_mayor_de_edad(self):
        return self._edad >= 18

class Cuenta:
    
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
        
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"Titular: {self.__titular.mostrar()}, Cantidad: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
        
    def es_titular_valido(self):
        return self.get_titular().es_mayor_de_edad() and self.get_titular().get_edad() < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Titular no válido para realizar la operación")
    
    def mostrar(self):
        print(f"Cuenta Joven. Bonificación: {self.__bonificacion}")


p2 = Persona("Daniel", 22, 39451265)
c2 = Cuenta(p2, 12500)
cj1 = CuentaJoven(p2, c2, 25)

cj1.retirar(500)