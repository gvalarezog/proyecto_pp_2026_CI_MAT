from datetime import date

from dominio.producto import Producto
from dominio.producto_digital import ProductoDigital
from dominio.producto_perecible import ProductoPerecible

arroz = Producto(codigo='A001', nombre='Arroz 2Kg', precio=2.30, stock=5)
yogourt = ProductoPerecible(codigo='Y001', nombre='Yogourt 15ml'
                                , precio=2, stock=15, fecha_vencimiento=date(2026,12,12))
leche = ProductoPerecible(codigo='L001', nombre='Leche 1Lt', precio=2
                        ,stock=5, fecha_vencimiento=date(2026,11,20))
pd1 = ProductoDigital(codigo='R002', nombre='Depositos de Banco del Barrio',
                      precio=0.50, url='https://www.bbarrio.fin.ec')
print(arroz)
print(yogourt)
# print('*'.center(50,'*'))
print(pd1)

productos = [arroz, yogourt, pd1, leche]

for producto in productos:
    print(f'{producto.nombre} - Precio de Venta: {producto.precio_venta()}')
    # if isinstance(producto, ProductoDigital):
    #     print('Producto Digital')
    # elif isinstance(producto, ProductoPerecible):
    #     print('Producto Perecible')
    # elif isinstance(producto, Producto):
    #     print('Producto')
    # else:
    #     print('Clase no valida')

# yogourt.precio = 3.00
# print(yogourt)
# yogourt.reponer(8)
# print(f'El nuevo stock es {yogourt.stock}')