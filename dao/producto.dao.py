import sys
sys.path.append(r'../')
from handdle.document import *
from model.producto import *

class DAOProducto:
    ##
    def save():
        ## dynamic data
        # produc = Producto(product.sku, product.nombre, product.descripcion, product.precio, product.stock)
        produc = Producto("SKU-05", 'Example1', 'This is an example1', 1000, 2222)
        
        ##Validamos la existencia del archivo => Obtenemos el nombre del documento
        fsDocName = Documento.validate('../datasource/', 'productos.json')
        response = Documento.write(fsDocName, produc)

        if response == True:
            return 'Producto guardado con exito'
    
    def read():
        ##
        route = '../datasource/productos.json'
        _productos = Documento.read(route)
        return _productos
    
    def drop(_id):
        ##
        route = '../datasource/productos.json'
        _productos = Documento.read(route)

        ##Search
        i = 0
        deleted = False
        for Producto in _productos:
            ##Buscar el objeto
            if Producto['id'] == _id:
                deleted = True
            else:
                i += 1

        ##Validar si NO SE ENCONTRO EL _id
        if deleted == False:
            print('El _id que se esta intentando buscar, NO EXISTE!!')

        ##Delet object from collection
        del _productos[i]

        print('New data:\n', _productos)

        ##Sobre-escribir la data en static_file
        Documento.write(route, _productos, True)
        
        ##
        return 'Producto borrado con exito'
    
    def consult(_id):
        ##
        route = '../datasource/productos.json'
        _productos = Documento.read(route)

        for Producto in _productos:
            ##Buscar el objeto
            if Producto['id'] == _id:
                return Producto
    
    def update(data):
        route = '../datasource/productos.json'
        _productos = Documento.read(route)

        ##
        _id = data['id']

        ##Traemos la data del producto en especifico
        for Producto in _productos:
            ##Buscar el objeto
            if Producto['id'] == _id:
                return Producto


DAOProducto.drop()
        