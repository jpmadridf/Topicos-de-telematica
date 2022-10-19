# info de la materia: ST0263 <Topicos en telematica>
#
# Estudiante(s): Juan Pablo Madrid Florez, jpmadridf@eafit.edu.co
#
# Profesor: EDWIN NELSON MONTOYA MUNERA, emontoya@eafit.edu.co
#
# <Lab 3>
# 1. breve descripción de la actividad
Desarrollar habilidades en el proceso de creación, despliegue y gestión de una aplicacion monolitica con balanceo y datos distribuidos, utilizando docker y aprender a asignar un certificado ssl válido a un dominio en Let's Encrypt. 
<texto descriptivo>
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
TODOS

Funcionales: 
- Desplegar la instancia en GCP
- Utilizar Wordpress
- Utilizar Docker
- Utilizar nginx
- Utilizar certbot
- Certificacion SSL
- Utilizar mysql
- Utilizar NFS


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Se utilizo:
- Gninx 
- Wordpress
- Cerbot
- Docker
- Mysql
- NFS

Se adquirio un dominio en freedom el cual fue jpmadridf.tk

Todo fue desarrolador en VM de GCP con Ubuntu 20.04, (1 LB, 2 Wordpress, 1 MYSQL, 1 NFS)

## como se compila y ejecuta.
Para ejecutar este proyecto se debe de inicializar la instacia en GCP y acceder de las siguientes formas:
- IP LB: 34.135.176.149
- DNS: lab4.jpmadridf.tk

## detalles del desarrollo.
Con el cumplimiento de la guia, primero creamos una maquina virtual para el baleanceador de cargas de NGINX, luego se configura el NFS, luego la DB y por ultimos los 2 wordpress de esta instancia instalamos Certbot, nginx, se configura la IP elastica con el dominio, se crea el certifciado SSL, luego de esto mediante docker instalamos Wordpress.

## detalles técnicos
Para este laboratorio debiamos contar mininmo con 5 instancia de GCP, que tuviera certbot, nginx y wordpress, habilitacion de el puerto 80, certificado SSL y un dominio, se creo el registro DNS y el registro del sitio web.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Se configura una IP elastica
La IP elastica es: 34.135.176.149
Un dominio: lab4.jpmadridf.tk
Se realiza la apertura de trafico en los siguientes puertos
Protocolo: TCP


# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Se utilizo GCP
En una instacia se desplego una VM con Ubuntu Server 20.04
Se descargo:
- Gninx
- Certbot
- Wordpress
- SSL
- Docker
- MySQL
- NFS

# IP o nombres de dominio en nube o en la máquina servidor.
La IP elastica es: 34.135.176.149 en protocolo http

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
IP: 34.135.176.149
Protocolo: TCP


## como se lanza el servidor.
El servido es una instancia de GCP, se debe de inicializar la instancia.
Una vez inicializada se puede accerder mediante:
- La IP: 34.135.176.149
- DNS: lab4.jpmadridf.tk


# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## Referencias para el lab: 
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
- https://www.letscloud.io/community/how-to-set-up-an-nginx-with-certbot-on-ubuntu
- https://geekrewind.com/setup-lets-encrypt-wildcard-on-ubuntu-20-04-18-04/
- https://linuxhint.com/install-and-configure-nfs-server-ubuntu-22-04/