import os
import json
from types import SimpleNamespace

class Documento:
    ##Valida la existencia del archivo, si no crearlo : Returns a JSON
    def validate(directory, name):
        ##
        dirRoute = directory + name

        try:
            ##Validar y/o obtener
            file = open(dirRoute)
            return file.name
        except FileNotFoundError:
            ##Crear documento vacio
            with open(os.path.join(directory, name), 'w') as file:
                json.dump({},file)
                return file.name

    ##Escribimos en el documento
    def write(route, data):
        try:
            ##
            data = json.dumps(data.__dict__)
            data = json.loads(data)

            ##Obtener la data del JSON del document [LECTURA]
            file = open(route, 'r')
            _rows = json.load(file)
            file.close()

            ##validar si la data esta vacia
            if _rows: ##Data-Llena
                ##Validar si la data obtenida es un array o un objeto
                if isinstance(_rows, list): ###Array
                    print('es un array')
                    ##Pushear el nuevo objeto al [array]
                    _rows.append(data)
                else: ###Object
                    _collection = []
                        
                    ##Pusheamos la data extraida
                    _collection.append(_rows)
                    ##Pusheamos la nueva data
                    _collection.append(data)

                    ##Setteamos
                    _rows = _collection
            else: ##Data-Vacia
                ##Setteamos el objeto (NUEVO) al JSONFile
                _rows = data
                
            ##Escribir / Sobrescribir la data en el archivo estatico
            file = open(route, 'w')
            file.write(json.dumps(_rows, indent=4))
            file.close()   
        except:
            print('Ah ocurrido un error al intentar escribir en documento')