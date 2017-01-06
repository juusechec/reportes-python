#!/usr/bin/env python3
class Reporte:

    def __init__(self):
        self.dir_imagenes = "imagenes" # no usado

    def generar_reporte1(self, url_imagen, formato):
        from mapas import descargar_imagen

        resultado = descargar_imagen(url_imagen=url_imagen)
        nombre_imagen = resultado["nombre_imagen"]
        dir_imagen = resultado["dir_imagen"]
        # print("nombre_imagen", nombre_imagen)
        # print("dir_imagen", dir_imagen)

        from mapas import consultar_arcgis
        numero_features = consultar_arcgis()
        from mapas import generar_docx
        nombre_imagen_sin_ext = nombre_imagen.split(".")[0]
        # filename.split(".")[-1] for extension
        nombre_archivo = nombre_imagen_sin_ext + ".docx"
        nombre_archivo_docx = generar_docx(
            nombre_archivo, dir_imagen, numero_features=numero_features, NombreProducto="SOME FEATURES NAME")
        print("nombre_archivo_docx", nombre_archivo_docx)
        if formato == "pdf":
            from mapas import exportar_a
            nombre_archivo_pdf = exportar_a(nombre_archivo_docx, formato)
            print("nombre_archivo_pdf", nombre_archivo_pdf)
            return nombre_archivo_pdf
        elif formato == "odt":
            from mapas import exportar_a
            nombre_archivo_odt = exportar_a(nombre_archivo_docx, formato)
            print("nombre_archivo_odt", nombre_archivo_odt)
            return nombre_archivo_odt
            #print(os.path.dirname(__file__), nombre_archivo, formato)
            #return send_file(nombre_archivo, as_attachment=True)
        elif formato == "docx":
            return nombre_archivo_docx

    def generar_reporte2(self, url_imagen):
        return "En construcción"
