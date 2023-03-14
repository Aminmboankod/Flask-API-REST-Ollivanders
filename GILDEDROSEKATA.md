# Gilded-Rose-Kata

# Índice

+   [Introducción](#introducción)
+   [Documentación para DDD](#documentación-para-el-domain-drive-design)
+   [Manual](#manual)
    +   [Requisitos previos](#requisitos-previos)
    +   [Instalación](#instalación)
+   [Modelo DDD](#modelo-ddd)
+   [Diagrama UML](#diagrama-uml)
+   [Pruebas](#pruebas)
    +   [Coverage](#coverage)




# Introducción

Los ficheros que encontrarás en este repositorio son el resultado del kata "GILDED ROSE KATA" propuesto en la clase de programación de Grado Superior de desarrollo Web Intensivo(2022).
El reto es programar teniendo en cuenta TDD y DDD el inventario de una tienda de productos mágicos.

### Documentación para el Domain Drive Design:
----

Especificaciones en el repositorio de mi tutor @dfleta : [Gilded Rose Requirements](https://github.com/dfleta/Python_ejercicios/blob/master/Poo/GildedRose_Refactoring_TDD_Kata/GildedRoseRequirements.txt)

>Hola y bienvenido al equipo Gilded Rose. Como saben, somos una pequeña posada con una ubicación privilegiada en un
ciudad prominente dirigida por un amable posadero llamado Allison. También compramos y vendemos solo los mejores productos.
Desafortunadamente, nuestros productos se degradan constantemente en calidad a medida que se acercan a su fecha de caducidad. Nosotros
tenemos un sistema que actualiza nuestro inventario por nosotros. Fue desarrollado por un tipo sensato llamado
Leeroy, que se ha embarcado en nuevas aventuras. Su tarea es agregar la nueva función a nuestro sistema para que
podemos comenzar a vender una nueva categoría de artículos. Primero una introducción a nuestro sistema:

>- Todos los artículos tienen un valor SellIn que indica la cantidad de días que tenemos para vender el artículo.
>- Todos los artículos tienen un valor de Calidad que indica qué tan valioso es el artículo
>- Al final de cada día, nuestro sistema reduce ambos valores para cada artículo

>Bastante simple, ¿verdad? Bueno, aquí es donde se pone interesante:

>- Una vez que ha pasado la fecha de caducidad, la calidad se degrada el doble de rápido
>- La Calidad de un artículo nunca es negativa
>- "Brie añejo" en realidad aumenta en calidad a medida que envejece
>- La calidad de un artículo nunca es más de 50
>- "Sulfuras", al ser un objeto legendario, nunca tiene que ser vendido o baja en Calidad
>- "Pases entre bastidores", como el brie añejo, aumenta en calidad a medida que se acerca su valor SellIn;
>La calidad aumenta en 2 cuando hay 10 días o menos y en 3 cuando hay 5 días o menos, pero
La calidad cae a 0 después del concierto.

>Recientemente hemos contratado a un proveedor de artículos mágicos. Esto requiere una actualización de nuestro sistema:

>- Los artículos "conjurados" se degradan en calidad dos veces más rápido que los artículos normales

>Siéntase libre de realizar cualquier cambio en el método UpdateQuality y agregar cualquier código nuevo siempre que todo
todavía funciona correctamente. Sin embargo, no modifique la clase Item o la propiedad Items ya que pertenecen a la
duende en la esquina que se enfurecerá instantáneamente y te disparará porque no cree en el código compartido
propiedad (puede hacer que el método UpdateQuality y la propiedad Items sean estáticos si lo desea, cubriremos
para usted).

>Solo para aclarar, un artículo nunca puede tener un aumento de calidad superior a 50, sin embargo, "Sulfuras" es un
objeto legendario y como tal su Calidad es 80 y nunca se altera.

# Manual

## Requisitos previos
| Paquete | Versión |
|:----:|:----:|
|attrs | 22.2.0
| exceptiongroup | 1.1.0 
| iniconfig | 1.1.1 |
| packaging | 22.0 | 
| pluggy | 1.0.0 |
| pytest | 7.2.0 |
| tomli | 2.0.1

## Instalación

Crea el directorio donde vas a clonar el repositorio  y clonalo usando el siguiente comando:
```
$ mkdir ./Gilded-Rose-Kata
$ cd Gilded-Rose-Kata
$ git clone https://github.com/Aminmboankod/Gilded-Rose-Kata.git
```
Ejecuta el archivo de configuración:
```
$ ./setup.sh
```

## Modelo DDD
---
![DDD Model](/docs/images/DDDModel-gildedRose.drawio.png)

## Diagrama UML
---
![Diagrama UML](/docs/images/gildedRoseUML.drawio.png)
## Pruebas
---
![test](/docs/images/test.png)

## Coverage
---
![coverage](/docs/images/coverage.png)