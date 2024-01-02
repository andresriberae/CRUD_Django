---
title: "Creacion App Django"
author: "Ribera Andres"
date: "1/01/2023"
output: html_document
---

# Pasos para crear una app en Django

1. Crear un directorio
2. Crear un entorno de desarrollo
3. Instalamos las librerias 
    - instalamos Django
    - instalamos freeze
4. Creacion de nuestro proyecto

---


## 1. Creamos el directorio donde ira nuestro proyecto
Creamos una directorio donde alojaremos nuestro proyecto.
* Ej: DjangoPoject/my_proyect

## 2. Crear un entorno de desarrollo
```
python -m venv env
```

*	Activamos nuestro **entorno virtual**
```
C:/DjangoPoject/my_proyect/env/Scripts> activate
(env) C:/DjangoPoject/my_proyect/env/Scripts>
```

## 3. Instalación de las librerias
### Instación de Django
```
pip install django
```

### Instación de Freeze
*	Instalamos una librería freeze para saber que librerías tenemos instaladas en nuestro entorno virtual.
```
pip install freeze
```

*	Para ejecutar la libreria:
```
pip freeze
```
* Usamos freeze para crear nuestro archivo de requerimientos
```
pip freeze > requirements.txt
```


## 4. Creamos nuestro proyecto
```
django-admin startproject config .
```

*	Para crear una aplicación Django
```
django-admin startapp myapp
```

## Crear un migraciones
```
python manage.py migrate
```
si se hace algun cambio en los modelos
```
python manage.py makemigrations
```

---
## Ejecutamos nuestro proyecto
```
python manage.py runserver
```



## Crear un superuser

```
python manage.py createsuperuser
```


# Ejecutar el docker
construimos la imagen 
```
docker build -t devrrior/docker-django .
```
creamos el contenedor en el puerto:
```
docker run -p 8000:8000 devrrior/docker-django
```
para poder ver los cambios en tiempo de ejecucion :
```
docker run -v /Users/hp/Desktop/DjangoProject/django_crud/:/app -p 8000:8000 devrrior/docker-django
```

para poder ver los cambios en tiempo de ejecucion y no ver todo el log con detach:
```
docker run -d -v /Users/hp/Desktop/DjangoProject/django_crud/:/app -p 8000:8000 devrrior/docker-django
```

para poder ver los logs
```
docker logs --follow <id_del_contendor>
```

para parar el docker
```
docker stop devrrior/docker-django
```

## para acceder dentro del contenedor
```
docker exec -it <id_del_contendor> /bin/sh
```