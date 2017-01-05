#!/usr/bin/env python3
from flask import send_file
from flask import send_from_directory
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return """
    Rutas configuradas: <br />
    <a href="/reporte">/reporte GET,POST</a>
    """


@app.route("/reporte/<format>", methods=['GET', 'POST'])
def reporte(format):
    import reporte
    import os
    dir_imagenes = "imagenes"
    resultado = reporte.guardar_imagen("dir_imagenes")
    nombre_imagen = resultado["nombre_imagen"]
    dir_imagen = resultado["dir_imagen"]
    # return send_file(dir_imagen, attachment_filename=nombre_imagen)
    from consultar_arcgis import consultar_arcgis
    numero_features = consultar_arcgis()
    from generar_docx import generar_docx
    nombre_archivo = generar_docx("nuevo.docx", dir_imagen, numero_features=numero_features, NombreProducto="SOME FEATURES NAME")

    try:
        if format == "pdf":
            from export_to import export_to
            nombre_archivo = export_to(nombre_archivo, format)
            print(os.path.dirname(__file__), nombre_archivo, format)
            return send_file(nombre_archivo, as_attachment=True)
        elif format == "odt":
            from export_to import export_to
            nombre_archivo = export_to(nombre_archivo, format)
            print(os.path.dirname(__file__), nombre_archivo, format)
            return send_file(nombre_archivo, as_attachment=True)
        elif format == "docx":
            return send_from_directory(os.path.dirname(__file__), nombre_archivo, as_attachment=True)
        else:
            print("Algo pasó")

        # return send_file(nombre_archivo, attachment_filename="reporte.docx")

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
