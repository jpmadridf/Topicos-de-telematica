# Información de la materia:

ST0263 - Tópicos Especiales en Telemática

# Estudiante:

Juan Pablo Madrid Florez, jpmadridf@eafit.edu.co

# Profesor:

Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad

Analisis del dataset de Covid-19 en Google Colab, por medio del dataframe PySpark y PySpark SQL. El analisis se hizo en dos jupyter notebooks distintos, uno con datos de origen en google drive y el otro en AWS S3.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor

- Importar datos de Google Drive y AWS S3.
- Hacer operaciones con el dataframe PySpark.
- Hacer operaciones con Pyspark SQL.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor

Todo lo propuesto ha sido implementado.

# 2. información general de diseño

- Drive: Servicio de almacenamiento de datos de Google.
- S3: Amazon Amazon S3 es un servicio de almacenamiento de objetos que ofrece escalabilidad, disponibilidad de datos, seguridad y rendimiento.
- PySpark: Framework de procesamiento de datos a alta escala.  

# 3. Descripción del ambiente de desarrollo y técnico:

## 0. Almacenar datos en Google Drive y S3

### Google Drive
- Subir los datos a drive:

![subuirdatosdrive](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/0/2.%20Datos%20en%20Drive.png)

### AWS S3
- Subir los datos a un bucket en S3:

![subirdatoss3](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/0/1.%20Datos%20en%20S3.png)

## 1. Cargar datos desde Google Drive y AWS S3

- **Nota**: Se realizan mas pasos que estan especificados en los documentos [ipynb](https://github.com/jpmadridf/Topicos-de-telematica/tree/main/Proyecto%203/ipynb).

### Google Drive

- Subir y verificar que si carguen los datos:

![prueba](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/1/2.%20Cargar%20desde%20Drive.png)

### AWS S3

- Subir y verificar que si carguen los datos:

![prueba](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/1/1.%20Cargar%20desde%20S3.png)

## 2. Análisis exploratorio del dataframe donde cargamos los datos

El analisis se hizo en dos notebooks distintos, cargando los datos desde Google Drive y AWS S3.

- Google Drive: [Proyecto_3_Drive.ipynb](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/ipynb/Proyecto_3_Drive.ipynb)

- AWS S3: [Proyecto_3_S3.ipynb](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/ipynb/Proyecto_3_S3.ipynb)


2.1) Columnas:

![columnas](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/2/1.%20Columnas.png)

2.2) Tipos de datos:

![tipodatos](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/2/2.%20Tipo%20de%20dato.png)

2.3) Seleccionar algunas columnas:

![seleccionarcolumnas](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/2/3.%20Seleccionar%20columnas.png)

2.4) Renombrar columnas:

![renombarcolumnas](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/2/4.%20Cambiar%20nombre%20de%20columna.png)

2.5) Agregar columnas:

![agregarcolumna](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/2/5.%20agregar%20columna.png)

2.6) Borrar columnas: 

![borrarcolumna](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/2/6.%20Borrar%20columna.png)

2.7) Filtrar datos:

![filtrardatos](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/2/7.%20Filtrar%20datos.png)

2.8) Ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva:

![lambda](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/2/8.%20Funcion%20lambda.png)


## 3. Contestar las siguientes preguntas sobre los datos de covid
3.1) Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor:

- Dataframe:

![1](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20DF/1..png)

- SparkSQL:

![1](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20Spark/1..png)

3.2) Las 10 ciudades con más casos de covid en Colombia ordenados de mayor a menor:

- Dataframe:

![2](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20DF/2..png)

- SparkSQL:

![2](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20Spark/2..png)

3.3) Los 10 días con más casos de covid en Colombia ordenados de mayor a menor:

- Dataframe:

![3](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20DF/3..png)

- SparkSQL:

![3](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20Spark/3..png)

3.4) Distribución de casos por edades de covid en Colombia:

- Dataframe:

![4](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20DF/4..png)

- SparkSQL:

![4](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20Spark/4..png)

3.5) Distribución de casos por estado:

- Dataframe:

![5](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20DF/5..png)

- SparkSQL:

![5](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/3.%20Spark/5..png)


## 4. Guardar los datos anteriores en AWS S3

- En el archivo con la conexion a AWS agregar las lineas:

![guardars3](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/4.%20Guarda%20datos%20en%20bucket/1.%20Guardar%20datos.png)

- Verificar que si se hayan guardado los datos en S3:

**URI:** s3://jpmadridfp3/proyecto3resultado/

![s3](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Proyecto%203/4.%20Guarda%20datos%20en%20bucket/2.%20Verificacion.png)


# 4. Información relevante

## Referencias:

- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata/03-spark
