import uuid

class Producto(object):
    def __init__(product, sku, nombre, descripcion, precio, stock):
        product.id = str(uuid.uuid4())
        product.sku = sku
        product.nombre = nombre
        product.descripcion = descripcion
        product.precio = precio
        product.stock = stock
    
    
    