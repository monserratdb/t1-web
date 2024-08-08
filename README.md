[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/UFP5mCQD)
# Tarea 1 :construction:

* :pencil2: **Nombre:** Monserrat Diaz
* :pencil2: **Correo:** mdb@uc.cl

## Código :symbols:

### :computer: Cómo ejecutar este código

```bash
# Indicar comandos necesarios para ejecutar la tarea
py Main.py
```

### :teacher: Explicación del funcionamiento del código 
El código utiliza Selenium para automatizar la navegación de la página wikidex y extrae información específica sobre cada pokemon pedido en el enunciado.

El programa se ejecuta desde Main.py porque este es el archivo principal, que importa las funciones necesarias desde Scrapper.py y Webdriver.py

En Main.py se encuentra la función execute_scrapping() que crea una instancia de la clase Scrapper que nos ayuda en la extracción de la información de los pokemons. También se crea una instancia de la clase WebDriver que la clase Scrapper utiliza para realizar la navegación en la página web y la extracción de datos.

En Web_driver.py se define la clase WebDriver y todas las funciones relacionadas al manejo de la página web, es decir, cambios de pestaña, iniciializar el driver, cargar páginas, hacer click en los elementos, cerrar una pestaña, entre muchas más.

Por otro lado, en Scrapper.py se define la clase Scrapper y todas las funciones necesarias para extraer la información de la página web utilizando la instancia de Webdriver de manera automática, en este caso: encontrar el pokemon solicitado en la página, extraer su información, guardar esta información en una lista de listas. Además de las funciones para crear el archivo .csv, lo que requiere que se cree una función para previamente ordenar los pokemons solicitados por peso para luego agregarlos a pokemons.csv

Con la creación del archivo pokemons.csv se cierra la ventana del navegador y se da por finalizado el programa. 


## Reflexión :thought_balloon:

### :scroll: ¿Cómo se usó DevTools para realizar la tarea?

DevTools se utilizó para inspeccionar los elementos de la página web y encontrar en dónde se encontraba la información relevante para lo solicitado.

Fue necesario revisar todo el código para encontrar los selectores CSS necesarios para identificar y extraer la información solicitada, es decir, identificar los elementos HTML que contenían esta información como los tipos, categorías, pesos, etc.

### :thinking: ¿Por qué necesaria la exploración previa con Devtool?

La exploración previa con DevTools fue necesaria para entender la estructura de la página web y así lograr que Selenium interactuara de manera correcta con los elementos de la página de forma efectiva para extraer la información solicitada.


### :adhesive_bandage: ¿Qué elementos en la página web podrían haber facilitado este desarrollo?

Algunos elementos que podrían haber facilitado el desarollo son el uso de identificadores únicos en los elementos HTML que contenían la información de los pokemons. También el que existiera una documentación clara que describiera la estructura de la página y los selectores CSS recomendados para acceder a la información. Y por último, el que hubiera una estructura HTML bien definida y coherente para que sea más fácil de navegar y extraer datos.