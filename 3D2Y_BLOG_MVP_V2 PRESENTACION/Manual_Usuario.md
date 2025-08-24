# 📚 MANUAL DE USUARIO - 3D2Y BLOG MVP V2

## 🎯 **Introducción**

Este manual de usuario está diseñado para ayudarte a utilizar todas las funcionalidades del **3D2Y Blog MVP Versión 2**. El sistema incluye herramientas avanzadas para la gestión de contenido, búsqueda inteligente y sistema de comentarios.

## 🚀 **Inicio Rápido**

### **Acceso al Sistema**
- **URL Principal**: http://127.0.0.1:8000/
- **Panel Admin**: http://127.0.0.1:8000/admin/
- **Credenciales**: admin / admin123

### **Navegación Principal**
- **🏠 Inicio**: Página principal del blog
- **📝 Blog**: Lista de todas las publicaciones
- **🔍 Búsqueda**: Buscar contenido específico
- **📊 Dashboard**: Panel de administración

## 👥 **Tipos de Usuario**

### **1. Visitantes (Público)**
- Pueden ver posts publicados
- Pueden buscar contenido
- Pueden agregar comentarios
- Pueden navegar por categorías

### **2. Administradores**
- Todas las funciones de visitantes
- Crear y gestionar posts
- Aprobar comentarios
- Acceder al panel administrativo
- Ver estadísticas del blog

## 🔍 **Sistema de Búsqueda (Nueva V2)**

### **Búsqueda desde el Header**
1. **Ubica** el formulario de búsqueda en la parte superior derecha
2. **Escribe** el término que deseas buscar
3. **Presiona** Enter o haz clic en el botón 🔍
4. **Revisa** los resultados mostrados

### **Búsqueda Avanzada**
1. **Ve a**: http://127.0.0.1:8000/search/
2. **Usa** el formulario central para búsquedas más específicas
3. **Explora** las búsquedas populares con los tags predefinidos
4. **Filtra** resultados según tus necesidades

### **Búsquedas Populares Disponibles**
- **Impresión 3D**: Posts sobre impresión 3D
- **Tutorial**: Guías y tutoriales
- **Tecnología**: Noticias tecnológicas
- **Modelado**: Diseño 3D y modelado

### **Consejos de Búsqueda**
- **Usa palabras clave** específicas
- **Combina términos** para resultados más precisos
- **Revisa sugerencias** si no encuentras resultados
- **Usa menos palabras** para búsquedas más amplias

## 💬 **Sistema de Comentarios (Nueva V2)**

### **Para Visitantes: Agregar Comentarios**

#### **Paso 1: Acceder a un Post**
1. **Ve al blog**: http://127.0.0.1:8000/blog/
2. **Haz clic** en cualquier post publicado
3. **Desplázate** hacia abajo hasta la sección de comentarios

#### **Paso 2: Completar el Formulario**
1. **Nombre**: Escribe tu nombre completo
2. **Email**: Ingresa tu dirección de email válida
3. **Comentario**: Escribe tu comentario (mínimo 10 caracteres)
4. **Observa** el contador de caracteres en tiempo real

#### **Paso 3: Enviar Comentario**
1. **Verifica** que todos los campos estén completos
2. **Haz clic** en "📤 Enviar Comentario"
3. **Espera** el mensaje de confirmación
4. **Ten en cuenta** que el comentario requiere aprobación

### **Para Administradores: Gestionar Comentarios**

#### **Aprobar Comentarios Individuales**
1. **Accede al admin**: http://127.0.0.1:8000/admin/
2. **Busca** la sección "Comentarios"
3. **Haz clic** en "Comentarios"
4. **Marca** la casilla "Aprobado" para el comentario deseado
5. **Haz clic** en "Guardar"

#### **Aprobar Comentarios Masivamente**
1. **Selecciona** múltiples comentarios usando las casillas
2. **Elige** "Aprobar comentarios seleccionados" del menú desplegable
3. **Haz clic** en "Ir"
4. **Confirma** la acción

#### **Rechazar Comentarios**
1. **Selecciona** los comentarios a rechazar
2. **Elige** "Rechazar comentarios seleccionados"
3. **Confirma** la acción

### **Filtros y Búsqueda de Comentarios**
- **Por estado**: Aprobado/No aprobado
- **Por fecha**: Ordenar por fecha de creación
- **Por post**: Filtrar comentarios de un post específico
- **Por autor**: Buscar comentarios por nombre

## ✏️ **Gestión de Contenido**

### **Crear Nuevos Posts**

#### **Método 1: Dashboard Rápido**
1. **Accede al dashboard**: http://127.0.0.1:8000/admin-dashboard/
2. **Haz clic** en "Crear Post"
3. **Completa** el formulario:
   - **Título**: Escribe un título atractivo
   - **Categoría**: Selecciona una categoría (opcional)
   - **Contenido**: Escribe el contenido del post
4. **Observa** el contador de caracteres
5. **Haz clic** en "📤 Publicar Post"

#### **Método 2: Panel Django Admin**
1. **Ve a**: http://127.0.0.1:8000/admin/
2. **Busca** la sección "Posts"
3. **Haz clic** en "Agregar Post"
4. **Completa** todos los campos requeridos
5. **Guarda** el post

### **Gestionar Posts Existentes**

#### **Desde el Dashboard**
1. **Accede** al dashboard administrativo
2. **Haz clic** en "Gestionar Posts"
3. **Para cada post** puedes:
   - **📤 Publicar**: Cambiar de borrador a publicado
   - **📥 Despublicar**: Cambiar de publicado a borrador
   - **🗑️ Eliminar**: Eliminar el post permanentemente

#### **Desde el Panel Admin**
1. **Accede** al panel Django Admin
2. **Selecciona** "Posts"
3. **Usa** las herramientas avanzadas de edición
4. **Aprovecha** los filtros y búsquedas

### **Estados de los Posts**
- **📄 Borrador**: Solo visible para administradores
- **✅ Publicado**: Visible para todos los visitantes
- **📁 Archivado**: Posts antiguos o descontinuados

## 📊 **Dashboard Administrativo**

### **Estadísticas en Tiempo Real**
- **Total de Posts**: Número total de publicaciones
- **Posts Publicados**: Posts visibles al público
- **Posts en Borrador**: Posts pendientes de publicación
- **Total de Categorías**: Categorías disponibles

### **Acciones Rápidas**
- **✏️ Crear Post**: Acceso directo al formulario de creación
- **📝 Gestionar Posts**: Administrar posts existentes
- **⚙️ Panel Admin**: Acceso al panel Django Admin
- **👁️ Ver Blog**: Vista previa del blog público
- **🚪 Cerrar Sesión**: Salir del sistema

## 🎨 **Personalización y Configuración**

### **Modo Oscuro/Claro**
1. **Busca** el botón "Modo oscuro" en el header
2. **Haz clic** para cambiar entre modos
3. **La preferencia** se guarda automáticamente

### **Navegación por Categorías**
1. **Usa** el sidebar para navegar por categorías
2. **Haz clic** en "📑 Categorías ▼" para expandir
3. **Selecciona** la categoría deseada
4. **Explora** los posts de esa categoría

## 🔧 **Solución de Problemas**

### **Problemas Comunes**

#### **No puedo acceder al sistema**
- **Verifica** que el servidor esté ejecutándose
- **Confirma** la URL: http://127.0.0.1:8000/
- **Revisa** las credenciales de acceso

#### **No puedo crear posts**
- **Verifica** que estés logueado como administrador
- **Completa** todos los campos requeridos
- **Revisa** que el contenido tenga al menos 50 caracteres

#### **No puedo agregar comentarios**
- **Asegúrate** de estar en un post publicado
- **Completa** todos los campos del formulario
- **Verifica** que el email tenga formato válido
- **Confirma** que el comentario tenga al menos 10 caracteres

#### **No veo mis comentarios**
- **Los comentarios** requieren aprobación del administrador
- **Contacta** al administrador para solicitar aprobación
- **Verifica** que el comentario se haya enviado correctamente

#### **La búsqueda no funciona**
- **Verifica** que hayas escrito el término correctamente
- **Prueba** con términos más generales
- **Revisa** que haya posts que coincidan con tu búsqueda

### **Contacto para Soporte**
- **Email**: admin@3d2yblog.com
- **Panel Admin**: http://127.0.0.1:8000/admin/
- **Documentación**: Revisa este manual completo

## 📱 **Uso en Dispositivos Móviles**

### **Características Responsive**
- **Navegación adaptativa** para pantallas pequeñas
- **Formularios optimizados** para touch
- **Imágenes responsivas** que se ajustan automáticamente
- **Menú colapsable** en dispositivos móviles

### **Consejos para Móviles**
- **Usa** el menú hamburguesa para navegar
- **Toca** los elementos para interactuar
- **Desplázate** horizontalmente si es necesario
- **Usa** el zoom para leer contenido pequeño

## 🎯 **Mejores Prácticas**

### **Para Administradores**
- **Revisa** comentarios regularmente
- **Mantén** contenido actualizado
- **Usa** categorías para organizar posts
- **Respalda** datos importantes
- **Monitorea** estadísticas del dashboard

### **Para Visitantes**
- **Lee** las políticas de comentarios
- **Sé respetuoso** en tus comentarios
- **Usa** la búsqueda para encontrar contenido
- **Explora** diferentes categorías
- **Comparte** contenido útil

## 📈 **Novedades de la Versión 2**

### **Funcionalidades Nuevas**
- ✅ **Sistema de búsqueda** global y avanzado
- ✅ **Sistema de comentarios** con aprobación
- ✅ **Formularios mejorados** con validación
- ✅ **Dashboard administrativo** con estadísticas
- ✅ **Diseño responsive** optimizado

### **Mejoras de Usabilidad**
- ✅ **Navegación más intuitiva**
- ✅ **Feedback visual mejorado**
- ✅ **Validación en tiempo real**
- ✅ **Mensajes de error más claros**
- ✅ **Accesibilidad mejorada**

---

## 🎉 **Conclusión**

El **3D2Y Blog MVP Versión 2** ofrece una experiencia completa para la gestión y consumo de contenido sobre impresión 3D y tecnología. Con las nuevas funcionalidades de búsqueda y comentarios, el sistema se ha convertido en una plataforma interactiva y fácil de usar.

**¡Disfruta explorando todas las funcionalidades del sistema!**

---

**Versión 2 - Agosto 2025**
**Manual de Usuario Completo**
