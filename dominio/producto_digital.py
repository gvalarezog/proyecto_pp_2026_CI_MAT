from dominio.descontable import Descontable
from dominio.producto import Producto


class ProductoDigital(Producto, Descontable):
    """
    Clase que representa una producto digital
    """
    def __init__(self, nombre, codigo, precio, url):
        super().__init__(nombre=nombre, codigo=codigo, precio=precio)
        self.__url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, nueva_url):
        self.__url = nueva_url

    def __str__(self):
        return f'Producto Digital [{self.__dict__.__str__()}]'

    def precio_venta(self):
        return self.aplicar_descuento(super().precio_venta())


if __name__ == '__main__':
    print(__name__)
    pd1 = ProductoDigital(codigo='R001', nombre='Restiros de Banco del Barrio',
                          precio=1.00, url='https://www.bbarrio.fin.ec')

    print(pd1)
    print(ProductoDigital.__mro__)

