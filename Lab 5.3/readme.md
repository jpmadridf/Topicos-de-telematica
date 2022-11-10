# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Juan Pablo Madrid Florez, jpmadridf@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Ejercicios básicos de MapReduce con MRJOB en python

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Resolver ejercicios usan MRJOB.
- Manejo de MRJOB con archivos..

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
Todo lo propuesto ha sido implementado.

# 2. información general de diseño
Resolver ejercicios del datasets usando python con MRJOB.

# 3. Descripción del ambiente de desarrollo y técnico:

## Detalles técnicos
- Python: es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.
- mrjob le permite escribir trabajos MapReduce en Python 2.7/3.4+ y ejecutarlos en varias plataformas.

## Descripción y cómo se configura los parámetros del proyecto

### Como compilar y ejecutar:
- Entramos a la carpeta del lab 5.3
```
cd "Lab 5.3/Codigo"
```

- Instalamos MRJOB
```
pip install mrjob
```

- Usamos el siguiente comando para ejecutar los ejercicios del punto 1, remplazando la X por el ejercicio que se quiere ejecutar:
```
python Codigo/p1/pX.py datasets/dataempleados.txt
```

- Usamos el siguiente comando para ejecutar los ejercicios del punto 2, remplazando la X por el ejercicio que se quiere ejecutar:
```
python Codigo/p2/pX.py datasets/dataempresas.txt  
```

- Usamos el siguiente comando para ejecutar los ejercicios del punto 3, remplazando la X por el ejercicio que se quiere ejecutar:
```
python Codigo/p3/pX.py datasets/datapeliculas.txt  
```
#### Nota
- En la carpte de imagenes podemos ver los resultados de cada ejercicios link: https://github.com/jpmadridf/Topicos-de-telematica/tree/main/Lab%205.3/Imagenes

# 4. Información relevante

## Referencias:
- https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/lab5-3-mrjob.txt
- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata/02-mapreduce
