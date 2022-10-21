import sys
sys.path.append(r'./')
from controller.producto_controller import *
from controller.vendedor_controller import *



class Principal:
    def main():
        ##Messages - Context
        modulo = 'Ingresar el numero/dato del modulo deseado.\n[1] - Vendedorens\n[2] - Productos\n[x] - Salir\n'
        option = 'Ingresa el numero/dato de la opcion deseada.\n'

        ##Messge - error
        moduloError = 'Modulo desconocido... Ingresar una accion valida'
        optionError = 'Opcion desconocida... Ingresar una accion valida'
        Seller = {}

        while(modulo != 'x' or option != 'x'):
            modulo = input(modulo)
            
            if modulo == '1': ##Vendedores
                options = '[1] - Usar\n[x] - Salir\n'
                option = option + options
                option = input(option)

                ##
                if option == '1':
                    ##
                    _vendedores = SellerController.leer()

                    print(_vendedores)

                    # ##Tabla [Vendedores]
                    # print('|    id    |    nombre    |')
                    # for Vendedor in _vendedores:
                    #     print('|    {Vendedor.id}    |    {Vendedor.nombre}    |')
                elif option == 'x':
                    exit(1)
                else:
                    print(optionError)
            elif modulo == '2': ##Productos
                options = '[1] - Crear\n[2] - Leer\n[3] - Eliminar\n[4] - Actualizar\n[5] - Vendedor\n[x] - Salir\n'
                option = option + options
                option = input(option)

                ##
                if option == '2':
                    ##
                    _products = ProductController.leer()
                    print(_products)

                    # ##Tabla [Vendedores]
                    # print('|    id    |    nombre    |')
                    # for Prod in _products:
                    #     print('|    {Prod.id}    |    {Prod.nombre}    |')
                # elif option == ''

                # elif option == ''

                # elif option == ''

                # elif option == ''
            elif modulo != "x":
                print(moduloError)
            
            if modulo == 'x' or option == 'x':
                exit(1)

Principal.main()