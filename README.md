# My 3D Blog

Un proyecto de blog 3D desarrollado con Django.

## Configuración del Entorno

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd my_3d_blog
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

4. **Ejecutar migraciones**
   ```bash
   python manage.py migrate
   ```

5. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

6. **Acceder a la aplicación**
   Abrir el navegador y visitar: http://127.0.0.1:8000/

## Estructura del Proyecto

```
my_3d_blog/
├── manage.py              # Script de gestión de Django
├── my_3D2Y_blog/         # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py        # Configuración del proyecto
│   ├── urls.py           # URLs principales
│   ├── wsgi.py           # Configuración WSGI
│   └── asgi.py           # Configuración ASGI
├── requirements.txt       # Dependencias del proyecto
└── README.md            # Este archivo
```

## Tecnologías Utilizadas

- **Django 5.2.5**: Framework web de Python
- **Python**: Lenguaje de programación principal
- **SQLite**: Base de datos (por defecto en desarrollo)

## Estado del Proyecto

- ✅ Configuración inicial del proyecto Django
- ✅ Entorno virtual configurado
- ✅ Dependencias instaladas
- ✅ Servidor de desarrollo funcionando

## Próximos Pasos

1. Crear aplicaciones Django específicas
2. Diseñar modelos de datos
3. Implementar vistas y templates
4. Configurar URLs
5. Implementar funcionalidades 3D

## Contribución

Para contribuir al proyecto, por favor sigue estos pasos:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
