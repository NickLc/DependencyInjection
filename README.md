
# Inyección de Dependencias

## 1. ¿Qué es inyección de dependencias?

## 2. Inyección de dependencias en python

### 2.1. Paquete dependency-injector PyPI
[dependency-injector](https://pypi.org/project/dependency-injector/)

## 3. ¿Cómo aplicamos al juego Space Invaders?

### 3.1. Componentes del juego

![Diagram](classDiagram.JPG)

### 3.2. Donde realizamos las inyecciones
La inyección de dependencias la realizamos en dos ocaciones: 
-Al momento en que se debe declarar el objeto PLAYER, que vendria a ser la nave que representa al jugador. En este caso esta nave puede tener tres modos de combate: fuego,hielo y veneno. Cada uno de estos modos tiene asociada una clase distinta y para suministrar los objetos de dichas clases existe un contenedor (en el archivo containers.py) preparado para proporcionarlos.
-Al momento de definir a los enemigos. Hay tres clases para cada tipo de enemigo (fuego, hielo, veneno) y sus objetos correspondientes son proveidos por el contenedor previamente mencionado.

## 4. ¿Cómo reproducir el juego?

### 4.1. Instalación

El juego requiere de los siguientes paquetes:
- dependency-injector
- pygame

Abrir su shell y realizar las siguientes comandos 
```sh
$ pip install dependency-inyector 
$ pip install pygame
```

### 4.2. Ejecución

1. Descargar el paquete
2. Ubicarse en el paquete
3. Abrir una shell 
4. Realizar el siguiente comando:
```sh
$ python main.py 
```

Nota: 
Verificar en su entorno de variables la palabra clave para ejecutar python, python3 o python

## 5. Demo 
Imagenes

Video de la demostración en el siguiente enlace: [demo](url)

