from datetime import date

from dominio.producto import Producto

class ProductoPerecible(Producto):
    """
    Clase que hereada de Producto para los perecibles
    """
    def __init__(self, nombre, stock, precio, codigo, fecha_vencimiento):
        super().__init__(nombre=nombre, codigo=codigo, precio=precio, stock=stock)
        self.__fecha_vencimiento = fecha_vencimiento

    @property
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, nueva_fecha):
        self.__fecha_vencimiento = nueva_fecha

    def __str__(self):
        return f'Producto Perecible [{self.__dict__.__str__()}]'

    def dias_por_vencer(self):
        return (self.__fecha_vencimiento - date.today()).days

    def precio_venta(self):
        base = super().precio_venta()
        if self.dias_por_vencer() <= 3:
            return round(base * 0.7, 2)
        return base

if __name__ == '__main__':
    yogourt = ProductoPerecible(codigo='Y001', nombre='Yogourt 15ml'
                                , precio=2, stock=15, fecha_vencimiento=date(2026,12,12))
    print(yogourt)
