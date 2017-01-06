# Proyecto de Generación de reportes con python

Se generan reportes PDF a partir de la implementación REST de los servicios de arcgis server o arcgis online.

# Dependencias

- Python >= 3.5
- python-arcgis-rest-query
- Flask *

# Pasos de instalación

1) Instalar una de las dependencias: (escriba los comandos preferiblemente en git-bash)

```bash
cd reportes-python # entrar al directorio descargado
git clone https://github.com/Schwanksta/python-arcgis-rest-query repo
```

2) Establece las variables de entorno para el usuario y el password de arcgis online:

- En Windows (cmd):

```bash
SET ARCGIS_USERNAME=usuario_arcgis_online
SET ARCGIS_PASSWORD=clave_arcgis_online
```

- En Windows (powershell):
```bash
$env:ARCGIS_USERNAME = "usuario_arcgis_online"
$env:ARCGIS_PASSWORD = "clave_arcgis_online"
```

- En GNU/Linux:

```bash
export ARCGIS_USERNAME='usuario_arcgis_online'
export ARCGIS_PASSWORD='clave_arcgis_online'
```
Opcionalmente agrega esas líneas en el ***~/.bashrc***

3) Cree unos directorios necesarios para el despliegue:
```bash
mkdir images
mkdir pdfs
```

4) Ejecutar el webservice:

```bash
python3 webservice.py
```
