# Sistema de Gestión de Tareas

Este proyecto es un sistema de gestión de tareas desarrollado con Django. Permite a los usuarios crear, actualizar, eliminar y marcar tareas como completadas. Además, incluye funcionalidades de autenticación y gestión de perfiles de usuario.

## Estructura del Proyecto

### base.html
Este archivo define la plantilla base del proyecto, que incluye:
- Metaetiquetas y enlaces a recursos externos como Bootstrap y CSS.
- Una barra de navegación responsiva que muestra enlaces de navegación dependiendo del estado de autenticación del usuario.
- Un bloque de contenido principal donde se renderizarán las diferentes vistas.
- Un pie de página con derechos de autor y un enlace a la página "About".

### Aplicación Tareas

#### urls.py
Define las rutas URL para la aplicación de tareas, incluyendo:
- Listado de tareas
- Detalle de una tarea específica
- Creación de nuevas tareas
- Actualización de tareas existentes
- Marcado de tareas como completadas
- Eliminación de tareas

#### views.py
Contiene las vistas basadas en clases para gestionar las tareas, tales como:
- ListadoTareaView
- DetalleTareaView
- CrearTareaView
- ActualizarTareaView
- CompletarTareaView
- EliminarTareaView

#### models.py
Define el modelo Tarea con campos para título, descripción, estado de completada, fecha de creación y actualización, y una relación con el usuario.

#### forms.py
Define el formulario TareaForm utilizado para crear y editar tareas.

### Aplicación Usuarios

#### urls.py
Define las rutas URL para la aplicación de usuarios, incluyendo:
- Inicio
- Login
- Logout
- Registro
- Ver perfil
- Editar perfil
- Cambiar contraseña
- Página "About"

#### views.py
Contiene las vistas para gestionar la autenticación y los perfiles de usuario, tales como:
- inicio
- login
- registro
- verPerfil
- editar_perfil
- cambiarPassword (visto como una clase)
- about

#### models.py
Define el modelo DatosExtra para almacenar información adicional del usuario, como el avatar.

#### forms.py
Define los formularios FormCreacion y EditarPerfil utilizados para el registro y la edición del perfil de usuario.

### Templates

#### usuarios

- **cambiar_password.html:** Formulario para cambiar la contraseña del usuario.
- **editar_perfil.html:** Formulario para editar el perfil del usuario, incluyendo el avatar.
- **login.html:** Formulario de inicio de sesión.
- **logout.html:** Mensaje de cierre de sesión.
- **principal.html:** Página de inicio del sistema de tareas.
- **registro.html:** Formulario de registro de nuevo usuario.
- **ver_perfil.html:** Muestra la información del perfil del usuario.

#### tareas

- **completar_tarea.html:** Formulario para marcar una tarea como completada.
- **confirmarEliminar_tarea.html:** Confirmación de eliminación de una tarea.
- **detalles_tarea.html:** Muestra los detalles de una tarea específica.
- **editar_tarea.html:** Formulario para editar una tarea existente.
- **index.html:** Lista todas las tareas del usuario.
- **tarea_nueva.html:** Formulario para agregar una nueva tarea.

## Uso

1. Regístrate o inicia sesión.
2. Crea, edita, completa o elimina tareas.
3. Gestiona tu perfil de usuario.