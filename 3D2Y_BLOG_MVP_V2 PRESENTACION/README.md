# My 3D Blog

Un proyecto de blog 3D desarrollado con Django siguiendo las mejores prácticas de estructura y organización.

## Configuración del Entorno

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Paracelso22/3D2Y_BLOG.git
   cd 3D2Y_BLOG
   ```

2. **Crear y activar el entorno virtual**
   ```bash
   # En Windows
   python -m venv venv
   venv\Scripts\activate
   
   # En Linux/macOS
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   # Copiar el archivo de ejemplo
   cp env.example .env
   
   # Editar las variables según tu entorno
   # DJANGO_ENVIRONMENT=development
   # SECRET_KEY=tu_clave_secreta_aqui
   ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   Abrir el navegador y visitar: http://127.0.0.1:8000/

## Estructura del Proyecto

```
my_3d_blog/
├── manage.py              # Script de gestión de Django
├── my_3D2Y_blog/         # Configuración principal del proyecto
│   ├── __init__.py
│   ├── urls.py           # URLs principales
│   ├── wsgi.py           # Configuración WSGI
│   └── asgi.py           # Configuración ASGI
├── settings/             # Configuraciones por entorno
│   ├── __init__.py       # Importación dinámica de settings
│   ├── base.py           # Configuraciones comunes
│   ├── development.py    # Configuraciones de desarrollo
│   └── production.py     # Configuraciones de producción
├── apps/                 # Aplicaciones Django
│   └── __init__.py
├── templates/            # Templates globales
│   └── base.html         # Template base
├── static/               # Archivos estáticos
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── requirements.txt       # Dependencias del proyecto
├── env.example           # Ejemplo de variables de entorno
├── .gitignore           # Archivos ignorados por Git
└── README.md            # Este archivo
```

## Configuración por Entornos

### Desarrollo
- `DEBUG = True`
- Base de datos SQLite
- Logging en consola
- Email backend de consola

### Producción
- `DEBUG = False`
- Base de datos PostgreSQL
- Configuraciones de seguridad
- Logging en archivos
- Email SMTP

## Tecnologías Utilizadas

- **Django 5.2.5**: Framework web de Python
- **Python**: Lenguaje de programación principal
- **SQLite**: Base de datos (desarrollo)
- **PostgreSQL**: Base de datos (producción)
- **Bootstrap 5**: Framework CSS
- **JavaScript**: Interactividad del frontend

## Estado del Proyecto

- ✅ Configuración inicial del proyecto Django
- ✅ Estructura organizada siguiendo mejores prácticas
- ✅ Configuración por entornos (desarrollo/producción)
- ✅ Templates y archivos estáticos configurados
- ✅ Entorno virtual configurado
- ✅ Dependencias instaladas
- ✅ Migraciones aplicadas
- ✅ Repositorio Git configurado

## Próximos Pasos

1. Crear aplicaciones Django específicas (users, blog, comments)
2. Diseñar modelos de datos
3. Implementar vistas y templates específicos
4. Configurar URLs de las aplicaciones
5. Implementar funcionalidades 3D
6. Configurar autenticación de usuarios
7. Implementar sistema de comentarios

## Variables de Entorno

Copia el archivo `env.example` a `.env` y configura las siguientes variables:

```bash
# Entorno de Django
DJANGO_ENVIRONMENT=development

# Clave secreta (cambiar en producción!)
SECRET_KEY=tu_clave_secreta_aqui

# Configuración de base de datos (producción)
DB_NAME=my_3d_blog
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432

# Configuración de email (producción)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_password_de_aplicacion
DEFAULT_FROM_EMAIL=tu_email@gmail.com

# Hosts permitidos (producción)
ALLOWED_HOSTS=localhost,127.0.0.1,tudominio.com
```

## Contribución

Para contribuir al proyecto, por favor sigue estos pasos:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
