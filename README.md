
# Proyecto Backend

Este es el backend de evaluacion-back-end Golden. En este repositorio encontrarás el código necesario para levantar el servidor y realizar la autenticación y gestión de datos.

## Requisitos

Asegúrate de tener instalados los siguientes programas:

- Python 3.x
- pip

## Pasos para ejecutar el proyecto

1. **Clonar el repositorio**

   Clona el repositorio en tu máquina local usando Git:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. **Crear el entorno virtual**

   Para crear un entorno virtual, ejecuta el siguiente comando en la raíz del proyecto:

   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**

   Una vez activado el entorno virtual, instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar el servidor**

   Para iniciar el servidor de desarrollo, ejecuta el siguiente comando:

   ```bash
   python manage.py runserver
   ```

   El servidor debería estar corriendo en `http://127.0.0.1:8000/`.

## Configuración de la base de datos
### En settings.py configurar la conexión a la base de datos. Por ejemplo, 
- DATABASES = {
- "default": {
  -     "ENGINE": "django.db.backends.postgresql",
  -     "NAME": "name",  # Nombre de la base de datos
  -     "USER": "user",    # Tu usuario de PostgreSQL
  -     "PASSWORD": "password",  # Tu contraseña de PostgreSQL
  -     "HOST": "127.0.0.1",  # Dirección IP del servidor de base de datos (local)
  -     "PORT": "5432",  # Puerto por defecto de PostgreSQL
- }
}


## Notas adicionales

- Si necesitas hacer migraciones en la base de datos, ejecuta:

  ```bash
  python manage.py migrate
  ```

- Si tienes dudas o problemas, revisa la documentación o abre un *issue* en este repositorio.

---

¡Disfruta trabajando con el proyecto!
