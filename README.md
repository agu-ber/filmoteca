# Filmoteca

En este proyecto, realicé una web donde se pueden visualizar algunas de mis películas, directores y actores preferidos. También es posible buscar e incluso añadir, editar y eliminar objetos en cada una de estas clases, mediante formularios. Cuenta con una básica vista de mensajería.
En cuanto a usuarios, pueden registrarse, loggearse, agregar un avatar, editar sus datos, enviar mensajes, etc.
En [este video](https://youtu.be/C49bUG0piHY) se puede ver en funcionamiento.

### Inicio

Para ingresar al inicio, debe ingresarse la ruta */* (luego de localhost:8000). Desde aquí, podremos acceder a cualquiera de las otras vistas, mediante la barra de navegación que se encuentra arriba. Para poder ingresar a las demás vistas, el usuario debe estar loggeado.

### Login y Sign up

Desde el inicio, se puede acceder a estas vistas. Se puede crear un usuario para luego ingresar con su contraseña correspondiente.

### Vistas de clases

Las vistas de clases son similares entre sí. En las tres tenemos un header con un título y una breve descripción de la vista. 
Debajo de este, encontraremos un botón que nos lleva a la vista para añadir un objeto (ej: */peliculas/añadir*).
Luego, tenemos un pequeño buscador, para encontrar algún objeto en particular.
Finalmente, se listan todos los objetos de dicha clase, con sus atributos.

### Vistas para añadir

Estas vistas pueden ser accedidas mediante los botones previamente explicados, o manualmente cambiando la ruta. En ellas, tenemos un formulario donde se pide llenar todos los campos, con los atributos correspondientes.
Finalmente, el formulario se envía con el botón *Añadir* y el objeto queda cargado en la base de datos.

### Vistas para editar y eliminar

Estas vistas son fácilmente accesibles desde las vistas de clases. Se pueden editar los datos de los objetos e incluso eliminarlos. 
Para los usuarios, es posible agregar o editar datos que desde el sign up no se podía, como ser nombre, apellido o avatar. Incluso es posible cambiar la contraseña (sabiendo la contraseña actual). 
### Vistas de resultados

Estas vistas pueden ser accedidas utilizando el buscador previamente explicado. Se mostrarán los resultados que coincidan con lo ingresado.

### Vista de mensajes

Los usuarios loggeados podrán enviar mensajes de texto desde aquí, no mayores a 100 caracteres. Estos se visualizarán todos en la misma vista, donde figura quién y en qué fecha y hora se envió el mensaje, lo que le da la impresión de un chat grupal.

### Panel de administración

Desde aquí se pueden modificar los objetos de las clases y los usuarios muy fácilmente.
El usuario es *admin* y la contraseña es *admin*.


**NOTA**: la base de datos viene casi vacía en cuanto a objetos de clases, solo se mantuvo el superusuario admin.