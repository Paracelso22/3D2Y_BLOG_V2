# 📚 MANUAL DE USUARIO - 3D2Y BLOG MVP

## 🚀 Instalación Rápida

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o extraer el proyecto**
   ```bash
   # Navegar al directorio del proyecto
   cd 3D2Y_BLOG_MVP
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Aplicar migraciones de base de datos**
   ```bash
   python manage.py migrate
   ```

4. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

6. **Acceder al proyecto**
   - Abrir navegador en: `http://127.0.0.1:8000/`

## 🔑 Credenciales de Acceso

### Usuario Administrador (Pre-configurado)
- **Usuario:** `admin`
- **Contraseña:** `admin123`
- **Email:** `admin@3d2yblog.com`

## 📱 Funcionalidades Principales

### 🏠 Página Principal
- **URL:** `http://127.0.0.1:8000/`
- **Descripción:** Página de inicio con hero section y posts destacados
- **Características:** 
  - Diseño responsive
  - Modo oscuro/claro
  - Navegación intuitiva

### 👤 Panel de Administración

#### Dashboard Principal
- **URL:** `http://127.0.0.1:8000/admin-dashboard/`
- **Funcionalidades:**
  - Estadísticas en tiempo real
  - Acceso rápido a funciones
  - Métricas de posts y categorías

#### Crear Posts
- **URL:** `http://127.0.0.1:8000/quick-create/`
- **Funcionalidades:**
  - Formulario rápido de creación
  - Selección de categorías
  - Publicación inmediata

#### Gestionar Posts
- **URL:** `http://127.0.0.1:8000/manage-posts/`
- **Funcionalidades:**
  - Ver todos los posts (publicados y borradores)
  - Cambiar estado (publicar/despublicar)
  - Eliminar posts
  - Editar contenido

#### Panel Admin Django
- **URL:** `http://127.0.0.1:8000/admin/`
- **Funcionalidades:**
  - Gestión avanzada de modelos
  - Configuración del sistema
  - Administración de usuarios

### 📝 Funcionalidades Públicas

#### Lista de Blog
- **URL:** `http://127.0.0.1:8000/blog/`
- **Características:**
  - Vista de todos los posts publicados
  - Filtrado por categorías
  - Paginación automática

#### Detalle de Post
- **URL:** `http://127.0.0.1:8000/blog/<slug>/`
- **Características:**
  - Vista completa del post
  - Contador de vistas
  - Navegación entre posts

#### Posts por Categoría
- **URL:** `http://127.0.0.1:8000/categoria/<id>/`
- **Características:**
  - Filtrado por categorías específicas
  - Contador de posts por categoría

#### Páginas Estáticas
- **Acerca de:** `http://127.0.0.1:8000/about/`
- **Contacto:** `http://127.0.0.1:8000/contact/`

### 🔐 Autenticación

#### Login
- **URL:** `http://127.0.0.1:8000/accounts/login/`
- **Características:**
  - Formulario de login personalizado
  - Redirección automática post-login

#### Logout
- **URL:** `http://127.0.0.1:8000/accounts/logout/`
- **Características:**
  - Cierre de sesión seguro
  - Redirección a página principal

## 🎨 Características de Diseño

### Modo Oscuro/Claro
- **Activación:** Botón "Modo oscuro" en el header
- **Persistencia:** Se mantiene la preferencia durante la sesión

### Diseño Responsive
- **Móviles:** Optimizado para pantallas pequeñas
- **Tablets:** Adaptación automática
- **Desktop:** Vista completa con sidebar

### Navegación
- **Header:** Acceso rápido a funciones principales
- **Sidebar:** Navegación por categorías
- **Footer:** Información de contacto y copyright

## 🔧 Funcionalidades Técnicas

### CRUD Completo
- ✅ **CREATE:** Creación de posts con formulario
- ✅ **READ:** Visualización de posts y listados
- ✅ **UPDATE:** Edición de estados y contenido
- ✅ **DELETE:** Eliminación de posts

### Gestión de Estados
- **Publicado:** Visible para todos los usuarios
- **Borrador:** Solo visible para administradores

### Sistema de Categorías
- **Organización:** Posts agrupados por categorías
- **Filtrado:** Navegación por categorías específicas
- **Colores:** Cada categoría tiene su color distintivo

## 🚨 Solución de Problemas

### Error: "No module named 'django'"
```bash
pip install django
```

### Error: "Database is locked"
```bash
# Detener el servidor (Ctrl+C)
# Reiniciar el servidor
python manage.py runserver
```

### Error: "Template does not exist"
```bash
# Verificar que todos los archivos están presentes
# Revisar la estructura de directorios
```

### Error: "Static files not found"
```bash
python manage.py collectstatic
```

## 📞 Soporte

Para problemas técnicos o consultas sobre el proyecto:
- **Desarrollador:** Paracelso22
- **Email:** akashaska22@gmail.com
- **Proyecto:** 3D2Y Blog MVP

---

**¡Disfruta usando 3D2Y Blog!** 🎉
