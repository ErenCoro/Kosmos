# Reconocimiento de entidades nombradas con Python 3.8
Crear una API REST sencilla que reciba una lista de oraciones en español y
devuelva una lista de las entidades nombradas identificadas en cada oración.

## Instalación

Instale las bibliotecas necesarias usando el administrador de paquetes. [pip](https://pip.pypa.io/en/stable/).

```bash
pip install Flask
pip install -U pip setuptools wheel
pip install -U spacy

```
## Ejecución 
Descargar la carpeta llamada project_API, una vez descargada situarse dentro de ella y ejecutar la instrucción 
```bash
python app.py
```
se puede hacer uso del servicio Postman para hacerle peticiones a la API 

## Uso
API desarrollada en Flask la cual recibe un JSON con una lista llamada "oraciones" de oraciones en español  y regresa JSON con una lista llamada "resultado" la cual contiene las oraciones, las entidades indentificadas en cada oración junto con el tipo de entidad. 



## Licencia
Desarrollada por Erendira Corona Bermúdez
