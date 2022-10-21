import uuid

class Venta:
    def __init__(sale, _idSeller, _idProduct, cantidad):
        sale.id = uuid.uuid4()
        sale._idSeller = _idSeller
        sale._idProduct = _idProduct
        sale.cantidad = cantidad