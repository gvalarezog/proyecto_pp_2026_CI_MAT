
archivo_r = None
try:
    with open('productos.txt', 'r') as archivo_r:
        for linea in archivo_r.readlines():
            print(linea)
except Exception as e:
    print(e)
finally:
    if archivo_r:
        archivo_r.close()