import sys
sys.path.append(r'../')
from handdle import document
from model.producto import *

class DAOProducto:
    directory = '../datasource/'
    document = 'producto.json'

    ##
    def save():
        # Producto(product.sku, product.nombre, product.descripcion, product.precio, product.stock)
        produc = Producto('SKU-01', 'LECHE', 'PRODUCTO LACTEO', 10, 100)

        print(produc.nombre)

DAOProducto.save()
        