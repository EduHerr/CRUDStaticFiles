import sys
sys.path.append(r'../')
from handdle.document import *

route = "../datasource/vendedores.json"

class DAOVendedor:
    def read():
        ##
        _sellers = Documento.read(route)
        return _sellers

    def consult(_id):
        ##
        _sellers = Documento.read(route)

        for Vendedor in _sellers:
            ##Buscar el objeto
            if Vendedor['id'] == _id:
                return Vendedor