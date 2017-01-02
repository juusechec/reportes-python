import json
import requests
import os


class Printer:
    """
    Una clase que permite imprimir un mapa dentro de unos parámetros
    """

    def __init__(self,
                 print_url='https://sampleserver6.arcgisonline.com/arcgis/rest/services/Utilities/PrintingTools/GPServer/Export%20Web%20Map%20Task/execute'):
        self.print_url = print_url

    def get_image(self, f="json", Format="PNG32", Layout_Template="MAP_ONLY",
                  Web_Map_as_JSON=''):
        params = {
            'f': f,
            'Format': Format,
            'Layout_Template': Layout_Template,
            'Web_Map_as_JSON': Web_Map_as_JSON
        }
        response = requests.get(self.print_url, params=params)
        json = response.json()
        imagen = json["results"][0]["value"]["url"]
        return imagen
