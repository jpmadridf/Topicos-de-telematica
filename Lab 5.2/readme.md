# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Juan Pablo Madrid Florez, jpmadridf@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Gestion de archivos HDFS mediante HUE y S3.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Desplegar cluster en EMR.
- Activacion de HUE.
- Creacion de usuario hadoop.
- Manejo de archivos mediante HUE.
- Manejo de archivos mediante SSH.
- Envio de arhcivos a S3 mediante HUE.
- Envio de archivos a S3 mediante SSH.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
Todo lo propuesto ha sido implementado.

# 2. información general de diseño
Se utilizo AWS para la creacion del cluster en EMR posteriomente se activa HUE con usuario hadoop, se accede a SSH mediante una instacia EC2 para el manejo de archivos
a su vez se utiliza HUE para la verificacion de esto, se crean buckets en S3 para un almacenamiento con persistencia.

# 3. Descripción del ambiente de desarrollo y técnico:

## Detalles técnicos
- AWS: servicio para desplegar las instancias.
- HUE: es una interfaz de usuario web para la gestión de Hadoo.
- EMR: es una plataforma de clúster administrada.
- Hadoop: entorno de trabajo para software, bajo licencia libre, para programar aplicaciones distribuidas que manejen grandes volúmenes de datos.
- S3: es un servicio ofrecido por Amazon Web Services que proporciona almacenamiento de objetos a través de una interfaz de servicio web. 

## Descripción y cómo se configura los parámetros del proyecto 

### Nota aclaratoria sobre los comandos
- En toda la documentacion dentro de cada imagen podemos ver los comandos utilizados durante cada proceso.

### Crear un cluster en EMR en AWS:
- Acceder a la consola de AWS.
- Dar click en **EMR**.
- Dar click en **Crear Cluster**.
- Dar click en **CREAR**.

### Manejo de archivos mediante HUE:
- Una vez el Cluster este desplegado, accedemos a HUE mediante internet.
- Dentro de HUE vamos a la carpeta de **files**.
![Files](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/HUE/1.%20Entramos%20a%20files.png)
- Creamos un directorio.
![Directorio](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/HUE/2.%20Se%20crea%20un%20directorio.png)
- Una vez creado el directorio, seleccionamos la opcion de **upload** y seleccionamos los archivos que deseamos subir.
![Archivos](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/HUE/3.%20Se%20selecciona%20el%20archivo%20a%20subir.png)
- Se suben los archivos a HUE en la seccion de files dentro de nuestro directorio.
![Archivos en HUE](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/HUE/4.%20Se%20suben%20los%20archivos.png)
- Se selecciona alguno para visualizar la informacion.
![Informacion](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/HUE/5.%20Permite%20la%20visualizacion%20de%20los%20archivos.png)

### Manejo de archivos mediante SSH:
- Accedemos a nuestra instancia EC2 que pertenezca al **MASTER**.
- Una vez dentro de la instancia mostramos los directorios de HUE.
![Directorios HUE](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/SSH/1.%20Mostrar%20directorios.png)
- Dentro de la instancia debemos de crear un directorios **datasets** donde almacenaremos los archivos de forma local.
- Mostramos los directorios de local.

![Directorios locales](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/SSH/2.%20Mostrar%20directorios%20local%20con%20datasets.png)
- Creamos un directorio en HUE de datasets.

![Directorio datasets HUE](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/SSH/3.%20creacion%20directorio%20en%20hadoop%20de%20datasets.png)
- Realizamos la copia de local a HUE con los comandos al directorio creado en HUE.
- NOTA: En el segundo comando podemos ver HUE nos dice que estos archivos ya fueron copiados en el primer comando.
![Copia de local a HUE](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/SSH/4.%20Copia%20de%20local%20a%20HUE.png)
- Revisamos que la copia se realizara de forma exitosa.
![Archivos en el directorio de HUE](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/SSH/5.%20Lista%20de%20datasets%20en%20hadoop.png)
- Creamo un directorio llamado **mis_datasets** en el local para enviar ahora los archivos de HUE a local.
- Una vez creamos el directorio enviamos los archivos.
- NOTA: En el segundo comando podemos ver HUE nos dice que estos archivos ya fueron copiados en el primer comando.
![Copia de arhcivos de HUE a local](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/SSH/6.%20Copiar%20desde%20HDFS%20hacia%20local.png)
- Mostramos los archivos copiados en local dentro de nustro directorio mis_datasets.
![Arhcivos en directorio local](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.2/SSH/7.%20Lista%20de%20archivo%20que%20se%20copiaron.png)

### Manejo de archivos desde HUE a S3:
- Entrar a HUE y seleccionar la pestaña de S3.
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
