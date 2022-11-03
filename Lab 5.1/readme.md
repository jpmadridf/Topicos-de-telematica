# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Juan Pablo Madrid Florez, jpmadridf@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Crear un Cluster AWS EMR en Amazon con activacion de HUE con usuario hadoop.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Desplegar cluster en EMR.
- Activacion de HUE.
- Creacion de usuario hadoop.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
Todo lo propuesto ha sido implementado.

# 2. información general de diseño
Se utilizo AWS para la creacion del cluster en EMR posteriomente se activa HUE con usuario hadoop.

# 3. Descripción del ambiente de desarrollo y técnico:

## Detalles técnicos
- AWS: servicio para desplegar las instancias.
- HUE: es una interfaz de usuario web para la gestión de Hadoo.
- EMR: es una plataforma de clúster administrada.
- Hadoop:  entorno de trabajo para software, bajo licencia libre, para programar aplicaciones distribuidas que manejen grandes volúmenes de datos.

## Descripción y cómo se configura los parámetros del proyecto 
### Crear un cluster en EMR en AWS:
- Acceder a la consola de AWS.
- Dar click en **EMR**.
- Dar click en **Crear Cluster**.
- Dar click en **CREAR**.

### Configuracion de Cluster:
- Se selecciona la version del cluster.
![Version](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.1/1.%20Version%206.3.1.png)
- Se selecciona las herramientas.
![Herramientas](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.1/2.%20Seleccion%20de%20herramientas.png)
- Se habilitan las vistas.
![Vistas](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.1/3.%20Se%20habilitan%20las%20vistas.png)
- Se modifica el tamaño.
![Tamaño](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.1/4.%20Se%20modifica%20a%20m4xlarge.png)
- Se configura la autoterminacion y el tamaño del cluster.
![Configuracion final](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.1/5.%20Se%20crea%20que%20se%20auto%20termine%20y%20se%20da%2020%20gb.png)

### Creacion Bucket:
- En S3 se crea un bucket.
![Bucket](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.1/6.%20Creacion%20de%20bucket.png)

### Conexion a puTTY:
- Se genera conexion al cluster master mediante puTTY
![Conexion](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.1/7.%20Conexion%20a%20cluster%20mediante%20putty.png)

## Configuración de HUE:

### Creacion de usuario hadoop:
- Se crea el usuario hadoop con la clave de preferencia.
![Usuario](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.1/8.%20Creacion%20usuario.png)

### Activacion de  HUE:
- Se inicia sesion y se ve HUE funcional.
![Activacion](https://github.com/jpmadridf/Topicos-de-telematica/blob/main/Lab%205.1/9.%20Pagina%20HUE.png)

# 4. Información relevante

## Referencias:
- https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/lab5-1-aws-emr.txt
- https://www.youtube.com/watch?v=MyXSwxN5Zdk
- https://www.youtube.com/watch?v=3sao-qJG34Y
