"""
Carga recursivamente el módulo
"""


def load_src(name, fpath):
    import os
    import imp
    try:
        return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
    except NameError:
        import sys
        is_windows = hasattr(sys, 'getwindowsversion')
        if (is_windows):
            fpath = fpath.replace('/', '\\')
        return imp.load_source(name, os.path.join(os.getcwd(), fpath))
load_src("arcgis", "../repo/arcgis/arcgis.py")

import arcgis
import os

def consultar_arcgis():
    # source = "https://services7.arcgis.com/lUZlLTBKH3INlBpk/arcgis/rest/services/IRSP_V1/FeatureServer"
    # username = os.getenv('ARCGIS_USERNAME', None)
    # password = os.getenv('ARCGIS_PASSWORD', None)
    # OBJECTID = "FID"  # la fila OBJECTID no está en el servicio
    # service = arcgis.ArcGIS(source,
    #                         username=username,
    #                         password=password,
    #                         object_id_field=OBJECTID)
    # layer_id = 0
    # geojson = service.get(layer_id)
    # print(geojson)

    source = "https://services7.arcgis.com/lUZlLTBKH3INlBpk/arcgis/rest/services/IRSP_V1/FeatureServer"
    # username = os.getenv('ARCGIS_USERNAME', None)
    # password = os.getenv('ARCGIS_PASSWORD', None)
    username = os.getenv('ARCGIS_USERNAME', None)
    password = os.getenv('ARCGIS_PASSWORD', None)
    # OBJECTID = "FID"  # la fila OBJECTID no está en el servicio
    service = arcgis.ArcGIS(
        source,
        username=username,
        password=password
    )

    layer_id = 0
    geojson = service.get(layer_id)
    return len(geojson["features"])
