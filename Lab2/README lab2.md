# info de la materia: ST0263 <Topicos en telematica>
#
# Estudiante(s): Juan Pablo Madrid Florez, jpmadridf@eafit.edu.co
#
# Profesor: EDWIN NELSON MONTOYA MUNERA, emontoya@eafit.edu.co
#

# <Lab 2>
#
# 1. breve descripción de la actividad
En este laboratorio se espera utilizar RABBITMQ como un middleware de comunicacion entre un Prodcutor y Consumidor, y que este consumidor pueda mostrar los datos de forma interactiva haciendole analisis a una variable de un IOT.
<texto descriptivo>
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Funcionales: 
- Desplegar la instancia en AWS
- Utilizar como middleware RABBITMQ
- Utilizar un Consumidor y un Productor
- Utilizar una plataforma de procesamiento de datos IOT


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Tanto el consumidor como el productor se rralizaron en python, con uso de las siguientes librerias:
- pika
- random
- decode
- callbacks
- time
- requests

Todo fue desarrolador en VSC.

## como se compila y ejecuta.
Para ejecutar este proyecto se debe de inicializar las instancias en AWS,
Mediante la IP elastica inicar sesion en RABBITMQ y a su vez en Ubidots, Primero ejecutar el programa de productor realizado en py, esperar que los datos entre a RABBITMQ, una vez los datos se encuentre en RABBITMQ ejecutar el programa consumidor en py, por ultimo entraremos a Ubidots donde se mostraran las graficas de los datos enviados y procesados.
## detalles del desarrollo.
Con el cumplimiento de la guia, primero se creo la instancia en AWS, una vez la instancia estuviera activa se realizo dentro de esta la descarga de RABBITMQ, se procedio a configurar el espacio para que sirviera de middleware para nuestras aplicaciones, una vez RABBITMQ estuviera configurada, se realizo el Productor en python, se verifico que existiera conexion para que tuviera buen procesamiento de los datos, el siguiente paso fue realizar nuestro consumidor basandonos en la guia de Ubidtos, una vez se creara todo lo necesario en Ubidots, se procedio a la verificacion de salida de datos de forma interactvia en Ubidtos comparando con los que envia el Porductor y los que llegaban a RABBITMQ.

## detalles técnicos
Para este laboratorio debiamos contar mininmo con una instancia de AWS, que tuviera RABBITMQ, habilitacion de los puertos, 2 aplicaciones que sirvieran de productor y consumidor, y por ulitmo una plataforma para procesamiento de datos IOT.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Se configura una IP elastica
La IP elastica es: 23.23.151.188 
Se realiza la apertura de trafico en los siguientes puertos
Protocolo: TCP
Puertos: 
- 5672
- 15672

Se mide la variable humedad

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
El servicio de middleware fue realizado en una instacia de AWS
El sistema Operativo de la instacia es Ubuntu Server 22.04
El middleware se utilizo RABBITMQ 3.10.7
Tanto el Productor como el Consumidor fueron creados en Python 3.10.4
Libreria utilizadas 
- pika
- random
- decode
- callbacks
- time
- requests
El procesamiento de datos se realizo en la plataforma digital Ubidtos

# IP o nombres de dominio en nube o en la máquina servidor.
La IP elastica es: 23.23.151.188 en protocolo http

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
IP: 23.23.151.188
Protocolo: TCP
Puertos: 
- 5672
- 15672

## como se lanza el servidor.
El servido es una instancia de AWS, se debe de inicializar la instancia.

## una mini guia de como un usuario utilizaría el software o la aplicación

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## Referencia para Consumidor: https://help.ubidots.com/en/articles/569964-simulate-data-in-ubidots-using-python
## Referencia para Prodcutor: 