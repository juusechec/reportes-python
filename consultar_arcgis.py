def consultar_arcgis():
    def load_src(name, fpath):
        # problema! no sirve en linux :(
        import os
        import imp
        try:
            return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
        except NameError:
            dir = fpath.replace('/', '\\')
            return imp.load_source(name, os.path.join(os.getcwd(), dir))
    load_src("arcgis", "repo/arcgis/arcgis.py")

    import arcgis

    source = "https://services7.arcgis.com/lUZlLTBKH3INlBpk/arcgis/rest/services/IRSP_V1/FeatureServer"
    # username = os.getenv('ARCGIS_USERNAME', None)
    # password = os.getenv('ARCGIS_PASSWORD', None)
    username = "pruebasincige"
    password = "pruebasincige2016"
    # OBJECTID = "FID"  # la fila OBJECTID no está en el servicio
    service = arcgis.ArcGIS(source,
                            username=username,
                            password=password)
    layer_id = 0
    geojson = service.get(layer_id)
    return len(geojson["features"])
