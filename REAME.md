# Proyecto de Generación de reportes con python

Se generan reportes PDF a partir de la implementación REST de los servicios de arcgis server o arcgis online.

# Dependencias

- Python >= 3.5
- python-arcgis-rest-query
- Flask *

# Pasos de instalación

1) Instalar una de las dependencias:

```bash
git clone https://github.com/Schwanksta/python-arcgis-rest-query repo
```

2) Establece las variables de entorno para el usuario y el password de arcgis online:

- En Windows:

```bash
SET ARCGIS_USERNAME=pruebasincige
SET ARCGIS_PASSWORD=pruebasincigepassword
```

- En GNU/Linux:

```bash
export ARCGIS_USERNAME='pruebasincige'
export ARCGIS_PASSWORD='pruebasincigepassword'
```
Opcionalmente agrega esas líneas en el ***~/.bashrc***

3) Ejecutar el webservice:

```bash
python3 webservice.py
```
