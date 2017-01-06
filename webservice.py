#!/usr/bin/env python3
from flask import Flask
from flask import send_file
from flask import send_from_directory
from flask import request

"""
Ingresa al navegador con:
http://ip:5000/reporte/pdf?url_imagen=http://ip_serv/imagen.png
"""

app = Flask(__name__)


@app.route("/")
def hello():
    return """
    Rutas configuradas: <br />
    <a href="/reporte">/reporte GET,POST</a>
    """


@app.route("/reporte/<formato>", methods=['GET', 'POST'])
def reporte(formato):
    url_imagen = request.args.get('url_imagen')
    # print("url_imagen", url_imagen)
    from reportes import Reporte
    nuevo_reporte = Reporte()
    nombre_archivo = nuevo_reporte.generar_reporte1(
        url_imagen=url_imagen,
        formato=formato
    )
    print("nombre_archivo", nombre_archivo)
    if formato == "pdf":
        return send_file(nombre_archivo, as_attachment=True, attachment_filename="reporte.pdf")
    elif formato == "odt":
        return send_file(nombre_archivo, as_attachment=True, attachment_filename="reporte.odt")
    elif formato == "docx":
        return send_file(nombre_archivo, as_attachment=True, attachment_filename="reporte.docx")
        #return send_from_directory(os.path.dirname(__file__), nombre_archivo, as_attachment=True)
    else:
        return "Extensión de archivo incorrecta."

    # try:
    #     print()
    # except Exception as e:
    #     return str(e)

if __name__ == "__main__":
    # para produccion reemplazar por la IP correspondiente
    app.run(host="0.0.0.0", port="5000")
