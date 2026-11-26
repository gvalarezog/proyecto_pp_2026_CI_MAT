#Guillermo Valarezo G
#Juan Pueblo

class Producto:
    """
    Clase que crea objetos de tipo producto.
    """
    iva = 0.15
    def __init__(self, codigo:str, nombre:str, precio:float, stock:int=0):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def codigo(self):
        return self.__codigo

    # @codigo.setter
    # def codigo(self, nuevo_codigo:str):
    #     self.__codigo = nuevo_codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio:float):
        if nuevo_precio <= 0:
            raise ValueError('Precio no valido')
        self.__precio = nuevo_precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nueva_cantidad:int):
        if nueva_cantidad <= 0:
            raise ValueError('Stock no valido')
        self.__stock = nueva_cantidad

    def vender(self, cantidad:int):
        if cantidad > self.stock:
            return False
        # self.stock = self.stock - cantidad
        self.stock -= cantidad
        return True

    def reponer(self, cantidad:int):
        if cantidad < 0:
            return False
        self.stock += cantidad
        return True

    def valor_inventario(self):
        return self.__precio * self.__stock

    def precio_venta(self):
        return round(self.precio * (1 + Producto.iva), 2)

    def __str__(self):
        return (f'Producto [codigo:{self.__codigo}, nombre: {self.__nombre}, '
                f'precio: {self.__precio}, stock: {self.__stock}]')


if __name__ == '__main__':
    arroz = Producto(codigo='A001', nombre='Arroz 2Kg', precio=2.30, stock=5)
    azucar = Producto(nombre='Azucar 2Kg', codigo='A002', stock=10, precio=3)
    arroz.stock = 10
    print(arroz.valor_inventario())
    print(azucar.valor_inventario())
    # print(azucar.__nombre)
    print(azucar.nombre)
    if arroz.reponer(cantidad=5):
        print('Aumento el stock')
    else:
        print('No aumento el stock')
    print(arroz.stock)
    # print(arroz.__str__())
    print(arroz)
    # arroz.__stock = 20
    # arroz.set_stock(20)
    arroz.stock = 20
    print(arroz)
    # arroz.codigo = 'AZ003'
    print(arroz)
    # arroz.set_stock(-5)
    # arroz.stock = -5
    print(arroz)

    # arroz1 = Producto(codigo='A001', nombre='Arroz 2Kg', precio=2.30, stock=5)
    # print(arroz1.valor_inventario())
    # arroz1.precio = -5
    # arroz1.stock = "diez"
    # print('*'.center(50, '*'))
    # print(arroz1)
    # print(arroz1.valor_inventario())


