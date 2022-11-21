# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Juan Pablo Madrid Florez, jpmadridf@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Wordcount en Apache Spark EN AWS EMR 6.3.1

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Creacion de un Cluster EMR para activar HUE.
- Utilizacion de HIVE y SparkSQL en HUE.
- Ejecucion de wordcount con datos en HDFS y S3.
- Ejecucion de wordcount en JupyterHub con datos de S3.
- Replicacion y entendimiento de Data_processing_using_PySpark.ipynb.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
Todo lo propuesto ha sido implementado.

# 2. información general de diseño
Se utilizo AWS para la creacion del cluster en EMR posteriomente se activa HUE con usuario hadoop, se accede a SSH mediante una instacia EC2 para el manejo de archivos
a su vez se utiliza HUE para la verificacion de esto, se crean buckets en S3 para un almacenamiento con persistencia, se utiliza pyspark para procesamiento de datos tanto
en terminal como en Jupyter.

# 3. Descripción del ambiente de desarrollo y técnico:

## Detalles técnicos
- AWS: servicio para desplegar las instancias.
- HUE: es una interfaz de usuario web para la gestión de Hadoo.
- EMR: es una plataforma de clúster administrada.
- Hadoop: entorno de trabajo para software, bajo licencia libre, para programar aplicaciones distribuidas que manejen grandes volúmenes de datos.
- S3: es un servicio ofrecido por Amazon Web Services que proporciona almacenamiento de objetos a través de una interfaz de servicio web. 

## Descripción y cómo se configura los parámetros del proyecto 

### Parte 1:

1. ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en HDFS vía ssh en el nodo master.

2. ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida)  vía ssh en el nodo master.

3. ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.

#### Creacion de los archivos en local y en HUE:
- Se guardan los datos en el datasets.
![Archivos](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/1.%20Datos%20en%20local.png)

- Se guardan en HUE.
![Archivos](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/2.%20Se%20crea%20en%20hive%20datasets.png)
![Archivos](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/3.%20Se%20guardan%20en%20hive.png)


#### Ejecutar el wordcount por linea de comando 'pyspark' Interactivo en EMR con datos en HDFS vía ssh en el nodo master.:
- Se ejecuta la siguiente linea de comandos.
    ```
    $ pyspark
    >>> files_rdd = sc.textFile("hdfs:///user/hadoop/dataset/gutenberg-small/*.txt")
    >>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    >>> wc = wc_unsort.sortBy(lambda a: -a[1])
    >>> for tupla in wc.take(10):
    >>>     print(tupla)
    >>> wc.saveAsTextFile("hdfs:///tmp/wcout1")
    ```
  ![Resultado](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/3.1%20Resultado%20HIve.png)
  
- El archivo que se guarda en **/tmp/wcout1**.
![Files](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/4.%20archivo%20en%20tmp.png)

#### Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida)  vía ssh en el nodo master.

- Se crea el bucket en S3.
![Directorio](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/5.%20Se%20crea%20el%20bucket%20en%20S3.png)

- Se ejecuta la sigueinte linea de conmandos.
    ```
    $ pyspark
    >>> files_rdd = sc.textFile("s3://datasetslab6/datasets/gutenberg-small/*.txt")
    >>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    >>> wc = wc_unsort.sortBy(lambda a: -a[1])
    >>> for tupla in wc.take(10):
    >>>     print(tupla)
    >>> 
    >>> wc.saveAsTextFile("hdfs:///tmp/wcout2")
    ```

![Resultado](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/6.%20Se%20corre%20desde%20S3%20y%20se%20crea%20el%20tmp.png)

- El archivo que se guarda en **/tmp/wcout2**.
![Archivos en HUE](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/HUE/4.%20Se%20suben%20los%20archivos.png)

- Se selecciona alguno para visualizar la informacion.
![Informacion](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/7.%20Archivos%20en%20HUE.png)

#### ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.
- Se crea un bucket dentro de Jupyter.
- Corremos sc para activar Spark.
- Corremos los siguientes comandos para utilizar wordcount.
    ```
    # WORDCOUNT COMPACTO
    files_rdd = sc.textFile("s3://datasetslab6/datasets/gutenberg-small/*.txt")
    wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    wc = wc_unsort.sortBy(lambda a: -a[1])
    for tupla in wc.take(10):
        print(tupla)
    ```

- Corremos lo siguiente comandos apra recuperar los datos.
    ```
    #salvar los datos de salida, fijarse que no exista: hdfs:///tmp/wcout10
    wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout3")
    #si esta trabajando en aws (igual verifique que no exista previamente wcout10):
    wc.coalesce(1).saveAsTextFile("s3://datasetslab6/wcout2")
    ```
![Jupyter](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/8.%20Se%20realiza%20en%20Jupyter.png)

- Archivos guardados en HUE.
![Archivos HUE](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/8.1%20Se%20guarda%20en%20HUE.png)

- Archivos guardados en S3.
![Archivos S3](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab6/Parte%201/8.2%20Se%20guarda%20en%20S3.png)

### Parte 2:

#### Replique, ejecute y ENTIENDA el notebook: Data_processing_using_PySpark.ipynb con los datos respectivos.

- Se crea.
![S3 HUE](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20HUE/1.%20Entrar%20a%20HUE%20y%20estar%20en%20la%20pestana%20de%20S3.png)

- Se crea un bucket para el manejo de archivos.
![Bucket](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20HUE/2.%20Se%20crea%20un%20bucket.png)

-  Una vez creado el bucket, seleccionamos la opcion de **upload** y seleccionamos los archivos que deseamos subir.
![Upload de archivos](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20HUE/3.%20Se%20selecciona%20los%20archivos%20y%20se%20suben.png)

- Se guardan los archivos en HUE.
![Archivos HUE](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20HUE/4.%20Quedan%20los%20datos%20en%20S3.png)

- Se verifica la creacion del bucket y archivos en S3 en AWS.
![S3 AWS](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20HUE/5.%20Se%20revisa%20AWS.png)

### Manejo de archivos desde SSH a S3:
- Primero creamos un bucket en S3 para la recepcion de archivos.
-![Creacion bucket](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20SSH/0.%20Creacion%20de%20bucket.png)

- Accedemos a nuestra instancia EC2 que pertenezca al **MASTER**.
- Una vez dentro de la instancia mostramos los archivos locales.

![Archivos locales](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20SSH/1.%20Se%20conecta%20via%20SSH%20y%20se%20confirma%20la%20existencia%20de%20los%20archivos.png)

- Se envian los archivos locales a S3.
![Envio de archivos](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20SSH/2.%20Se%20realiza%20la%20copia%20a%20un%20nuevo%20bucket.png)

![Envio de archivos](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20SSH/2.1%20Se%20copian%20el%20resto%20de%20archivos.png)

- Se verifican en S3 la recepcion de los archivos.
![Verificacion](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/S3%20SSH/3.%20se%20confirma%20la%20existencia%20de%20los%20datos%20en%20S3.png)


# 4. Información relevante

## Referencias:
- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata/01-hdfs
- https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/01-hdfs/hdfs-scripts.txt
- https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/lab5-2-hdfs-s3.txt
