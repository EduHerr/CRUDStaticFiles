import sys
sys.path.append(r'../')
from handdle.document import *
from model.producto import *

route = "../datasource/productos.json"

class DAOProducto:
    ##
    def save(product):
        ## dynamic data
        produc = Producto(product['sku'], product['nombre'], product['descripcion'], product['precio'], product['stock'])
        
        ##Validamos la existencia del archivo => Obtenemos el nombre del documento
        fsDocName = Documento.validate('../datasource/', 'productos.json')
        response = Documento.write(fsDocName, produc)

        if response == True:
            return True
    
    def read():
        ##
        _productos = Documento.read(route)
        return _productos
    
    def drop(_id):
        ##
        
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
        return True
    
    def consult(_id):
        ##
        _productos = Documento.read(route)

        for Producto in _productos:
            ##Buscar el objeto
            if Producto['id'] == _id:
                return Producto
    
    def update(data):
        _productos = Documento.read(route)

        ##
        _id = data['id']

        ##Traemos la data del producto en especifico
        for idx, Producto in enumerate(_productos):
            ##Buscar el objeto
            if Producto['id'] == "6ce38aec-68ae-4c89-86f1-693434ca1fab":
                ##Update properties
                if data['sku'] != None:
                    Producto['sku'] = data['sku']
                
                if data['nombre'] != None:
                    Producto['nombre'] = data['nombre']
                
                if data['descripcion'] != None:
                    Producto['descripcion'] = data['descripcion']
                
                if data['precio'] != None:
                    Producto['precio'] = data['precio']
                
                if data['stock'] != None:
                    Producto['stock'] = data['stock']

                ##Modificar
                _productos[idx] = Producto
        
        ##Sobre-escribir la data en static_file
        Documento.write(route, _productos, True)

        return True       