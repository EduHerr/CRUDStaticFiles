import os
import json

class Document:
    ##Valida la existencia del archivo, si no crearlo
    def validateDocument(directory, Document):
        ##Get Document Route
        docName = Document.name
        dirRoute = directory + docName

        try:
            ##Validar
            file = open(dirRoute)
            print(file)
            file.close()
        except FileNotFoundError:
            ##Crear documento
            data = Document.data

            with open(os.path.join(directory, docName), 'w') as file:
                json.dump(data, file)
