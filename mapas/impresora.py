import json
import requests
import os


class Impresora:
    """
    Una clase que permite imprimir un mapa dentro de unos parámetros
    Para usar se necesita:
    impresora = mapas.imprimir.Impresora()
    gpstring = \"\"\"{"mapOptions":{"showAttribution":true,"extent":{"xmin":-8250416.766858629,"ymin":515917.1351499202,"xmax":-8246671.352472556,"ymax":519710.322678672,"spatialReference":{"wkid":102100}},"spatialReference":{"wkid":102100},"scale":18055.95482200396},"operationalLayers":[{"id":"defaultBasemap","title":"Topográfico","opacity":1,"minScale":591657527.591555,"maxScale":70.5310735,"url":"https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer"},{"id":"Geodatabase_Redes_CAN_4074","title":"Geodatabase Redes CAN - Poste_etb","opacity":1,"minScale":36112,"maxScale":0,"layerDefinition":{"drawingInfo":{"renderer":{"type":"simple","symbol":{"angle":0,"xoffset":0,"yoffset":0,"type":"esriPMS","url":"RedSphere.png","imageData":"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","contentType":"image/png","width":15,"height":15}}}},"token":"nXJ5hYlwUmLV6j-uI7eBc1tazQkaPpH9PBggdPJ9yJgBKxkj603WLfkplYF-x8eibMyKoGOQfj2Em6Cr_tZQuG1JgIJsgGwSW2Tt02DAqCCo13W_hnDzFJAOGAMdSQBZp3SJK2tQ9Zq3Dj8kYBsn8ktRXD-ehApQkTxQptwdcKlr7FWpg8uYEGgvjJ6z4qcm_L0JGcG2tsx3X8yUvpk1i3n11seuYJVQRQTXpFNpWEMylM2B6vSI2_8a8muKLll7ZbQnR7GF1zGUakYYi_2WLw..","url":"https://services7.arcgis.com/lUZlLTBKH3INlBpk/arcgis/rest/services/IRSP_V1/FeatureServer/0"},{"id":"graphicsLayer1","opacity":1,"minScale":0,"maxScale":0,"featureCollection":{"layers":[]}},{"id":"map_graphics","opacity":1,"minScale":0,"maxScale":0,"featureCollection":{"layers":[]}}],"exportOptions":{"outputSize":[670,500],"dpi":96},"layoutOptions":{"titleText":"","authorText":"","copyrightText":"","customTextElements":[],"scaleBarOptions":{},"legendOptions":{"operationalLayers":[]}}}\"\"\"
    url_imagen = impresora.obtener_imagen(Web_Map_as_JSON=gpstring)
    """

    def __init__(self,
                 print_url='https://sampleserver6.arcgisonline.com/arcgis/rest/services/Utilities/PrintingTools/GPServer/Export%20Web%20Map%20Task/execute'):
        self.print_url = print_url

    def obtener_imagen(self, f="json", Format="PNG32", Layout_Template="MAP_ONLY",
                  Web_Map_as_JSON=''):
        params = {
            'f': f,
            'Format': Format,
            'Layout_Template': Layout_Template,
            'Web_Map_as_JSON': Web_Map_as_JSON
        }
        response = requests.get(self.print_url, params=params)
        json = response.json()
        print(json)
        imagen = json["results"][0]["value"]["url"]
        return imagen
