
# Inyección de Dependencias

## Creación injector

Para poder reproducir el injector no se necesita instalar librerias, basta con ejecutar el siguiente comando:

```sh
$ python propio_Injector.py 
```

## 1. ¿Cómo reproducir el juego?

### 1.1. Instalación

El juego requiere de los siguientes paquetes:
- dependency-injector
- pygame

Abrir su shell y realizar las siguientes comandos 
```sh
$ pip install dependency-inyector 
$ pip install pygame
```

### 1.2. Ejecución

1. Descargar el paquete
2. Ubicarse en el paquete
3. Abrir una shell 
4. Realizar el siguiente comando:
```sh
$ python main.py 
```

Nota: 
Verificar en su entorno de variables la palabra clave para ejecutar python, python3 o python

## 2. Demo 
Imagenes

Video de la demostración en el siguiente enlace: [demo](https://www.youtube.com/watch?v=rkGRhB00AjA)


## 3. ¿Qué es inyección de dependencias?
La inyección de dependencias (ID) es una patron de diseño en ingeniería de software para definir las dependencias entre objetos. Básicamente, el proceso de suministrar un recurso que requiere una determinada pieza de código. El __recurso requerido__ se llama dependencia.

Hay varias clases y objetos definidos al escribir código. La mayoría de las veces, estas clases dependen de otras clases para cumplir con su propósito. Estas clases, o componentes, conocen los recursos que necesita y cómo obtenerlos. ID maneja la definición de estos recursos dependientes y proporciona formas de instanciarlos o crearlos externamente. 

Si el objeto A (cliente) depende del objeto B (servicio), el objeto A no debe crear el objeto de dependencia B directamente. En lugar de esto, el objeto A debe proporcionar una forma de inyectar el objeto B. La responsabilidad de la creación del objeto y la inyección de dependencia se delegan en __el código externo__.

## 3.2. ¿Por qué usar la inyección de dependencia en su código?

- Flexibilidad de los componentes configurables: como los componentes están configurados externamente, puede haber varias definiciones para un componente (Control en la estructura de la aplicación).
- Pruebas más fáciles: es más fácil crear instancias de objetos simulados e integrarse con varias clases.
- Alta cohesión: código con una complejidad reducida del módulo, mayor reutilización del módulo.
- Dependencias minimalistas: como las dependencias están claramente definidas, es más fácil eliminar / reducir dependencias innecesarias.

## 4. Inyección de dependencias en python

### 4.1. Paquete dependency-injector PyPI


Para aplicar DI en python usamos la librería [dependency-injector](https://pypi.org/project/dependency-injector/).

La inyección de dependencia, como patrón de diseño de software, tiene varias ventajas que son comunes para cada lenguaje (incluido Python): 

-	La inyección de dependencia se puede utilizar para externalizar los detalles de configuración de un sistema en archivos de configuración que permiten reconfigurar el sistema sin recompilarlo. Se pueden escribir configuraciones separadas para diferentes situaciones que requieren diferentes implementaciones de componentes. Reducción del código repetitivo en los objetos de la aplicación ya que todo el trabajo para inicializar o configurar dependencias es manejado por un componente proveedor.
-	La inyección de dependencia le permite al código cliente eliminar todo conocimiento de una implementación concreta que necesita usar. Esto ayuda a aislar al cliente del impacto de los cambios y defectos de diseño. Promueve la reutilización, la capacidad de prueba y la mantenibilidad.
-	 La inyección de dependencia le permite al código cliente la flexibilidad de ser configurable. Solo el comportamiento del cliente es fijo. El cliente puede actuar sobre cualquier cosa que admita la interfaz intrínseca que el cliente espera.


![code](readme_Image/code1.png)

DI utiliza providers y containers para realizar la inversión de dependencia:

- __Providers__ : Crea una nueva instancia de la clase especificada en cada llamado.
![provider](readme_Image/provider.png)

- __IoC Containers__: Los contenedores son colecciones de proveedores. El propósito principal de los contenedores es agrupar proveedores.
![container](readme_Image/container.png)

## 5. ¿Cómo aplicamos al juego Space Invaders?

### 5.1. Componentes del juego

![Diagram](readme_Image/classDiagram.JPG)

### 5.2. Donde realizamos las inyecciones
La inyección de dependencias la realizamos en dos ocaciones: 
- Al momento en que se debe declarar el objeto PLAYER, que vendria a ser la nave que representa al jugador. En este caso esta nave puede tener tres modos de combate: fuego,hielo y veneno. Cada uno de estos modos tiene asociada una clase distinta y para suministrar los objetos de dichas clases existe un contenedor (en el archivo containers.py) preparado para proporcionarlos.
- Al momento de definir a los enemigos. Hay tres clases para cada tipo de enemigo (fuego, hielo, veneno) y sus objetos correspondientes son proveidos por el contenedor previamente mencionado.

