from datetime import date

from dominio.producto import Producto
from dominio.producto_digital import ProductoDigital
from dominio.producto_perecible import ProductoPerecible

#crear objetos
arroz = Producto(codigo='A001', nombre='Arroz 2Kg', precio=2.30, stock=5)
yogourt = ProductoPerecible(codigo='Y001', nombre='Yogourt 15ml'
                                , precio=2, stock=15, fecha_vencimiento=date(2026,12,12))
leche = ProductoPerecible(codigo='L001', nombre='Leche 1Lt', precio=2
                        ,stock=5, fecha_vencimiento=date(2026,11,20))
pd1 = ProductoDigital(codigo='R002', nombre='Depositos de Banco del Barrio',
                      precio=0.50, url='https://www.bbarrio.fin.ec')
archivo =  None

#manejar excepcion para guardar objetos en el archivo
try:
    with open('productos.txt', 'a+') as archivo:
        archivo.write(f'Producto: {arroz}\n')
        archivo.write(f'Producto: {yogourt}\n')
        archivo.write(f'Producto: {leche}\n')
        archivo.write(f'Producto: {pd1}\n')
except Exception as e:
    print(e)
finally:
    if archivo:
        archivo.close()

for i in range(1,10):
    print(i)

