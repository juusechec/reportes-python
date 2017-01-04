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
    resultado = reporte.guardar_imagen("dir_imagenes")
    nombre_imagen = resultado["nombre_imagen"]
    dir_imagen = resultado["dir_imagen"]
    #return send_file(dir_imagen, attachment_filename=nombre_imagen)
    from export_to import export_to
    nombre_archivo = export_to(dir_imagen)
    try:
        return send_file(nombre_archivo, attachment_filename="reporte.pdf")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
