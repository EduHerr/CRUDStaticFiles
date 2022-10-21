import sys
sys.path.append(r'../')
from handdle.document import *
from model.producto import *

class DAOProducto:
    ##
    def save():
        ## dynamic data
        # Producto(product.sku, product.nombre, product.descripcion, product.precio, product.stock)
        produc = Producto('SKU-03', 'LECHE', 'PRODUCTO LACTEO', 10, 100)
        
        ##Validamos la existencia del archivo => Obtenemos el nombre del documento
        fsDocName = Documento.validate('../datasource/', 'productos.json')
        Documento.write(fsDocName, produc)

DAOProducto.save()
        