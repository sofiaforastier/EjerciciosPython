class Cuenta:

    def __init__(self, titular, cantidad):
        self.__titular = titular;
        self.__cantidad = cantidad;
        

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self.__cantidad = valor
       

    def mostrar(self):
        print('El titular de esta cuenta es {}'.format(self.titular));

    def ingresar(self,cantidad):
       if cantidad > 0:
        self.__cantidad += cantidad
                    
                  
    def retirar(self,cantidad):
        self.__cantidad -= cantidad

    def __str__(self):
        return 'titular: {}, cantidad {}'.format(self.titular, self.cantidad);

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, edad, bonificacion=1.0):
        super().__init__(titular, cantidad)
        self.edad= edad
        self.bonificacion= bonificacion

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @property
    def bonificacion(self):
        return self.__bonificacion * 1.0

    @bonificacion.setter
    def bonificacion(self, valor):
        self.__bonificacion= valor


    def es_titular_valido(self, edad):
        if edad > 18 and edad < 25:
            return True
        else:
             return False

    def Mostrar(self):
        print('Es cuenta Joven y posee bonificacion de : ', self.bonificacion , '%')
        

    def retirarDinero(self,cantidad):
        if self.es_titular_valido () == True:
            self.cantidad -= cantidad
        else:
            print('La operacion no es posible')


    
      

Cuenta1 = Cuenta('Sofia Forastier', 33000);
Cuenta2 = Cuenta('Lola Mora', 25000);
Cuenta3 = Cuenta('Juan Perez', 50000);
 
Cuenta4= CuentaJoven('Juana', 25669, 20, 30);
Cuenta5= CuentaJoven('Diego Lopez', 14000, 23, 30);
Cuenta6= CuentaJoven('Fito Garia', 50000, 21, 30);






