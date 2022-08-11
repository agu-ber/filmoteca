# Filmoteca

En este proyecto, realicé una web donde se pueden visualizar algunas de mis películas, directores y actores preferidos. También es posible buscar e incluso añadir objetos a cada una de estas clases, mediante formularios.

### Índice

Para ingresar al índice, debe ingresarse la ruta *filmoteca/* (luego de localhost:8000). Desde aquí, podremos acceder a cualquiera de las otras vistas, mediante la barra de navegación que se encuentra arriba.

### Vistas de clases

Las vistas de clases son similares entre sí. En las tres tenemos un header con un título y una breve descripción de la vista. 
Debajo de este, encontraremos un botón que nos lleva a la vista para añadir un objeto (ej: *filmoteca/peliculas/añadir*).
Luego, tenemos un pequeño buscador, para encontrar algún objeto en particular.
Finalmente, se listan todos los objetos de dicha clase, con sus atributos.

### Vistas para añadir

Estas vistas pueden ser accedidas mediante los botones previamente explicados, o manualmente cambiando la ruta. En ellas, tenemos un formulario donde se pide llenar todos los campos, con los atributos correspondientes.
Finalmente, el formulario se envía con el botón *Añadir* y el objeto queda cargado en la base de datos.

### Vistas de resultados

Estas vistas pueden ser accedidas utilizando el buscador previamente explicado. Se mostrarán los resultados que coincidan con lo ingresado.

### Panel de administración

Desde aquí se pueden modificar los objetos de las clases y los usuarios muy fácilmente.
El usuario es *admin* y la contraseña es *admin*.


**NOTA**: la base de datos viene con entradas cargadas para facilitar la visualización del sitio.