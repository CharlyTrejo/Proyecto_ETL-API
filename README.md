

# <h1 align=center> **PROYECTO DE DATA ENGINEER** </h1>

# <h1 align=center>**Plataformas de streaming**</h1>



Este repositorio es un proyecto INDIVIDUAL de  ***Data Engineering***. En el cual a partir de datasets de plataformas de streaming (Netflix, Amazon, Disney+ y Hulu) transformo datos y creo funciones de consulta para que estos puedan ser accedidos a través de una API de acceso público desplegada en DETA, la API fue construida con el framework FastAPI. 

<hr>  

## **Desarrollo del Proyecto**

## Transformación de Datasets

* Se generó el campo **id** , donde los valores se transformaron agregando la primer letra correspondiente a la plataforma a la cual pertenecen seguido del id que ya tenían, es decir si un registro corresponde a la plataforma de Netflix y su id era "s455", ahora su id será "ns455". De esta manera cada registro tendrá un id único entre todos los registros de todas las plataformas de streaming. 

* Los **valores nulos** del  campo 'rating' fueron reemplazados por el string "g" correspondiente al maturity rating "general for all audiences". 

* Todas las fechas presentes en los datasets fueron transformadas al formato **AAAA-mm-DD** .

* Todos los valores de tipo string fueron normalizados a minúsculas.

* El campo ' duration' se dividió en dos columnas: duration_int y duration_type. En donde el tipo de valor de duration_int se convirtió a un integer y el del segundo a un string. 

* Dentro del campo duration_type se normalizaron los valores (seasons , season) a season. 

Hoy en día contamos con **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.


## Desarrollo  de la API y deployment

* La construcción de la API la realicé con **FastAPI**, por ser un web framework moderno y de alto rendimiento para construir APIs con Python. 

* En tanto que el deployment lo realicé con Deta dada su accesibilidad, entorno amigale para desplegar API's construidas con FastAPI, además de ser un servicio gratuito.



## **Disposición del proyecto**

**`Datasets`**:  Dentro de esta carpeta se encuentran dos carpetas: 
* **datasets_originales** : Dentro de esta carpeta se encuentran los datasets sin modificaciones. 
 * **datasets_transformados**: Dentro de esta carpeta se encuentran los datasets en formato csv obtenidos a partir de las transformaciones cuyos métodos se encuentran en el archivo transformacion.ipynb

<br/>

**`transformacion.ipynb`**:  En este archivo se encuentran los métodos aplicados en los datasets originales para su transformación y exportación a archivos .csv. 

<br/>


**`main.py`**: En este archivo se encuentra la construcción de la API con el framework FastAPI,en el cual se encuentran los métodos empleados para obtener el resultado a una consulta hecha.  

<br/>

**`requirements.txt`**: librerias especificadas necesarias para el deployment de la API.


<br/>

## **Información de la API**
* Name: PI-CarlosTrejo
* runtime: python3.9
* endpoint: https://68bcz7.deta.dev 
       





