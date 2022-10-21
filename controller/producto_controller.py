import sys
sys.path.append(r'../')
from dao.producto_dao import *

class ProductController:
    def crear(data):
        response = DAOProducto.save(data)

        if response == True:
            return 'Producto guardado con exito'
    
    def leer():
        _items = DAOProducto.read()

        return _items

        # if(len(_items) > 0):
        #     return _items
        # else:
        #     return 'Productos insuficientes para mostrar'
        

    def eliminar(_id):
        response = DAOProducto.drop(_id)

        if response == True:
            return 'Producto borrado con exito'

    def actualizar(data):
        response = DAOProducto.update(data)
        
        if response == True:
            return 'Producto actualizado con exito'