class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    @property
    def get_nombre(self):
        return self.nombre 
    
    def set_nombre(self, nuevo_nombre):
        if(nuevo_nombre == ""):
            return "El nombre no puede estar vacio"
        else:
            self.nombre = nuevo_nombre
        
    
    @property
    def get_edad(self):
        return self.edad
    
    def set_edad(self, nueva_edad):
        if(nueva_edad<0):
            print("La edad no puede ser menor a 0, estar vacía o ser una cadena de texto")
        else:
            self.edad = nueva_edad

    @property
    def get_dni(self):
        return self.dni

    
    def set_dni(self, nuevo_dni):
        if(nuevo_dni <= 3000000):
            self.dni = self.dni
            print("El DNI no puede ser menor a 3.000.000")
        elif(len(str(nuevo_dni)) < 8):
            print("El DNI tiene que tener 8 digitos.")        
        self.dni = nuevo_dni

    @property  
    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")
    
    @property
    def es_mayor_de_edad(self):
        if (self.edad < 18):
            return False
        else:
            return True

persona1 = Persona("Roberto", 22, 37637065)

