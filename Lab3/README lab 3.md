# info de la materia: ST0263 <Topicos en telematica>
#
# Estudiante(s): Juan Pablo Madrid Florez, jpmadridf@eafit.edu.co
#
# Profesor: EDWIN NELSON MONTOYA MUNERA, emontoya@eafit.edu.co
#
# <Lab 3>
# 1. breve descripción de la actividad
En este laboratorio a traves de GCP instalamos un Wordpress usando docker y a la vez lo certificamos con SSL, mediante certbot y nginx 
<texto descriptivo>
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Funcionales: 
- Desplegar la instancia en GCP
- Utilizar Wordpress
- Utilizar Docker
- Utilizar nginx
- Utilizar certbot
- Certificacion SSL


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Se utilizo:
- Gninx 
- Wordpress
- Cerbot
- Docker

Se adquirio un dominio en freedom el cual fue jpmadridf.tk

Todo fue desarrolador en VM de GCP con Ubuntu 20.04

## como se compila y ejecuta.
Para ejecutar este proyecto se debe de inicializar la instacia en GCP y acceder de las siguientes formas:
- IP: 34.170.254.99
- DNS: www.jpmadridf.tk o jpmadridf.tk

## detalles del desarrollo.
Con el cumplimiento de la guia, primero creamos una maquina virtual en GCP, a su vez pedimos un dominio, se le instala Ubuntu 20.04, luego dentro de esta instancia instalamos Certbot, nginx, se configura la IP elastica con el dominio, se crea el certifciado SSL, luego de esto mediante docker instalamos Wordpress.

## detalles técnicos
Para este laboratorio debiamos contar mininmo con una instancia de GCP, que tuviera certbot, nginx y wordpress, habilitacion de el puerto 80, certificado SSL y un dominio, se creo el registro DNS y el registro del sitio web.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Se configura una IP elastica
La IP elastica es: 34.170.254.99
Un dominio: jpmadridf.tk
Se realiza la apertura de trafico en los siguientes puertos
Protocolo: TCP
Puerto: 
- 80

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Se utilizo GCP
En una instacia se desplego una VM con Ubuntu Server 20.04
Se descargo:
- Gninx
- Certbot
- Wordpress
- SSL
- Docker

# IP o nombres de dominio en nube o en la máquina servidor.
La IP elastica es: 34.170.254.99 en protocolo http

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
IP: 34.170.254.99
Protocolo: TCP
Puerto: 
- 80

## como se lanza el servidor.
El servido es una instancia de GCP, se debe de inicializar la instancia.
Una vez inicializada se puede accerder mediante:
- La IP: 34.170.254.99
- DNS: jpmadridf.tk o www.jpmadridf.tk


# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## Referencia para el lab: https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
