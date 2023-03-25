
# :repeat: PROJECTO OLLIVANDERS --> [ FLASK API REST ] 


En el siguiente repositorio se reutilizará el código del repositorio [Aminmboankod/Gilded-Rose-Kata](https://github.com/Aminmboankod/Gilded-Rose-Kata) (para más información [readme](./GILDEDROSEKATA.md)) para completar el proyecto de final del segundo trimestre de curso del grado superior `intensivo` de desarrollo de aplicaciones web que consiste en lo siguiente:



- [Indice](#)
   - [Instalación](#instalación)
   - [Uso](#uso)
   - [Dependencias](#dependencias)
      - [Pytest]()
      - [Coverage]()
      - [Tox](#tox)
      - [Docker]()




# Instalación

```
clone https://github.com/Aminmboankod/Flask-API-REST-Ollivanders
```
Crear archivo tar.gz que contiene el proyecto
````
python3 setup.py sdist
````

Para arrancar el proyecto en un contenedor Docker:
````
docker build -t ollivanders-api-image:latest .

docker run -p 5000:5000 ollivanders-api-image:latest
````


# Uso 
Para acceder a los distintos endpoints de esta API utilizando curl, puedes utilizar los siguientes comandos:

Obtener la lista de ítems del inventario:
```
curl http://127.0.0.1:5000/inventario
```

Actualizar un ítem del inventario (debes especificar el nombre del ítem en el body de la petición):
```
curl -X POST -H "Content-Type: application/json" -d '{"name":"nombre_del_item"}' http://127.0.0.1:5000/actualizar
```

Actualizar un ítem del inventario mediante el formulario (debes especificar el nombre, sell_in y quality del ítem en el body de la petición):
```
curl -X POST -F "name=nombre_del_item" -F "sell_in=valor_sell_in" -F "quality=valor_quality" http://127.0.0.1:5000/update-item
```
Recuerda reemplazar "nombre_del_item", "valor_sell_in" y "valor_quality" con los valores correspondientes.

# Dependencias
````
attrs==22.2.0
certifi==2022.12.7
charset-normalizer==3.1.0
click==8.1.3
coverage==7.2.1
exceptiongroup==1.1.1
Flask==2.2.3
idna==3.4
iniconfig==2.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
packaging==23.0
pluggy==1.0.0
pytest==7.2.2
requests==2.28.2
tomli==2.0.1
urllib3==1.26.15
Werkzeug==2.2.3
`````

# Tox 

Tox es una herramienta de automatización de tareas que se utiliza comúnmente en proyectos de Python para facilitar la ejecución de pruebas, comprobaciones de estilo y otras tareas relacionadas con el proyecto. 

-------------------------------------------------------------------------

`"A continuación el enunciado del proyecto escrito por mi tutor:"` [@dfleta](https://github.com/dfleta/ollivanders_shop)

# Ollivanders wands shop




Como la demanda de productos mágicos no para de crecer, la expansión del negocio es inevitable para sobrevivir a Amazon. 

Ollivander había contratado a Dobbie -a través del programa de FP Dual DAW de Hogwarts colegio concertado- para que le hiciese una app que gestionase el inventario, pero tras los tristes aoontecimientos en los que se vió -desgraciadamente- envuelto el pobrecico elfo, no tiene a nadie que pueda modificar el código para incluir nuevos productos.

![Gif animado de Dobby](https://media.giphy.com/media/S33oo9EWdlZHW/giphy.gif "Dobby refactorizando")

Ollivander ha contratado los servicios de la consultora en la que trabajas para que adecúe la aplicación a las nuevas necesidades del inventario, por lo que te envían "a cliente" -a la tienda- a lidiar con él y, lo que es peor, con el código spagheti que manufacturó Dobby en sus momentos de langidez infinita.

Por si no fuera suficiente, tu compañero de empresa al que enviaron a cliente antes que a ti, a acaba de irse de España porque en el extranjero le pagan por trabajar, y ha dejado tiritando el código de los casos test que intentó añadir en un día de desesperación absoluta.

## Tareas a realizar

### Lógica

1. Refactoriza el código de la lógica para que sea fácil de entender, barato de modificar y no cambie el comportamiento observable del código existente.
2. El código existente pasa los casos test. Asegúrate de que el tuyo también, sin modificarlos.
3. Haz un evolutivo del sistema para que sea posible añadir al inventario un nuevo tipo de item llamado "_Conjured_". Los “_Conjured_” items degradan su calidad el doble de rápido que un item normal. Añade esta lógica al sistema así como los casos test que necesites.

**WARNING**: no alteres la clase `Item` o las propiedades de `Items`  porque el colegio profesional de goblings no cree en la propiedad compartida del código y suele enviar inquisidores por la tienda de vez en cuando para chequear no dos sino tres, digo tres cosas sino cuatro, no cuatro sino cinco cosas, _oh f*ck!_ que han de respetar su certificación de _gobbling inside_.

Aquí está el **repo donde Dobbie publicó el código**, que en realidad es el repo de Emily Bache con el **kata de refactorización "Gilded Rose"** para varios lenguajes:
https://github.com/emilybache/GildedRose-Refactoring-Kata

Las **reglas de la lógica del negocio** están "explicadas" aquí:
http://iamnotmyself.com/2011/02/14/refactor-this-the-gilded-rose-kata/ 

Aquí los **casos test**:
https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/master/texttests/ThirtyDays


### Base de datos

1. Crea una base de datos SQL que permita realizar CRUD sobre el inventario.
2. El inventario inicial es el que especifica el primer caso test, el existente en el "día 0". Recuerda realizar un esquema que permita ampliarlo con el nuevo tipo de ítem "_Conjured_":
   
```
name, sellIn, quality
+5 Dexterity Vest, 10, 20
Aged Brie, 2, 0
Elixir of the Mongoose, 5, 7
Sulfuras, Hand of Ragnaros, 0, 80
Sulfuras, Hand of Ragnaros, -1, 80
Backstage passes to a TAFKAL80ETC concert, 15, 20
Backstage passes to a TAFKAL80ETC concert, 10, 49
Backstage passes to a TAFKAL80ETC concert, 5, 49
Conjured Mana Cake, 3, 6
```

### App web

Como quieres modernizar un poco el sistema de gestión de la tienda de Ollivander, decides desarrollar una app web que permita visualizar el estado del inventario, actualizar la calidad de los items y realizar operaciones básicas CRUD.

Esto supone tres capas en tu aplicación.

1. Capa de presentación y _frontend_.
   - Utilizando HTML, CSS y JS construye un pequeño sitio web para la intranet, con una interfaz de usuario/a que permita a Ollivander realizar las operaciones de la lógica. 
2. Capa de lógica y _backend_
   - En el back encapsularás la lógica del negocio que has programado. Utilizarás un microframework llamado Flask para:
     - Atender y responder las peticiones que lleguen a través de un navegador web con las consulas de a la base de datos.
     - Construir una API REST que con al menos dos _end points_: un recurso devuelve el inventario y el otro la actualización del inventario. Si implementas el resto de operaciones CRUD, tendrás que añadir los _end points_ correspondientes.
3. Acceso a datos (_backend_)
   - Mediante Flask, escribe el código necesario de la capa de acceso a datos, que conecte las peticiones web con la base de datos, para realizar las operaciones de la lógica. Recuerda que la lógica de la aplicación ha de ser agnóstica respecto a la base de datos utilizada.
4. Base de datos: reutiliza tus conocimientos de Mongo Atlas del primer trimestre, o aprovecha para implementar una base de datos relacional con MySQL.
5. Pensando en introducir un flujo de trabajo de Integración Continua y Entrega Continua (CI /CD) prepararás un contenedor [Docker](https://www.docker.com/ "Docker") de desarrollo y pruebas y otro contenedor docker para despliegue. De momento, con Python es suficiente [tox](https://tox.readthedocs.io/en/latest/ "tox")



























