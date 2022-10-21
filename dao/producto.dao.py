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
    
    def update():
        route = '../datasource/productos.json'
        _productos = Documento.read(route)
        Product = {}

        ##
        # _id = data['id']

        ##Traemos la data del producto en especifico
        for idx, Producto in enumerate(_productos):
            ##Buscar el objeto
            if Producto['id'] == "6ce38aec-68ae-4c89-86f1-693434ca1fab":
                ##Update properties
                # if data['sku'] != None:
                #     Producto['sku'] = data['sku']
                
                # if data['nombre'] != None:
                #     Producto['nombre'] = data['nombre']
                
                # if data['descripcion'] != None:
                #     Producto['descripcion'] = data['descripcion']
                
                # if data['precio'] != None:
                #     Producto['precio'] = data['precio']
                
                # if data['stock'] != None:
                #     Producto['stock'] = data['stock']

                Producto['nombre'] = 'LH420'

                ##Modificar
                _productos[idx] = Producto
        
        ##Sobre-escribir la data en static_file
        Documento.write(route, _productos, True)
            
        


DAOProducto.update()
        