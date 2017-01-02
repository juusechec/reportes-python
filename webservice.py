#!/usr/bin/env python3
from flask import send_file
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    Rutas configuradas: <br />
    <a href="/reporte">/reporte GET,POST</a>
    """

@app.route("/reporte", methods=['GET', 'POST'])
def reporte():
    import reporte
    import os
    dir_imagenes = "imagenes"
    nombre_imagen = reporte.guardar_imagen("dir_imagenes")["nombre_imagen"]
    dir_imagen = reporte.guardar_imagen("dir_imagenes")["dir_imagen"]
    return send_file(dir_imagen, attachment_filename=nombre_imagen)
    try:
        return send_file("arcgis.pdf", attachment_filename="python.pdf")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
