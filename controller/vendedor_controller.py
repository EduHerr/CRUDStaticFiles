import sys
sys.path.append(r'../')
from dao.vendedor_dao import *

class SellerController:
    def leer():
        _items = DAOVendedor.read()
        return _items
    
    def consultar(_id):
        Seller = DAOVendedor.consult()
        return Seller