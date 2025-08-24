from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    """Modelo para categorías de posts"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    color = models.CharField(max_length=7, default='#003366')  # Color para la categoría
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    """Modelo para posts del blog"""
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]
    
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    resumen = models.TextField(max_length=300, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen_principal = models.ImageField(upload_to='posts/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='borrador')
    likes = models.IntegerField(default=0)
    vistas = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

class Tag(models.Model):
    """Modelo para etiquetas de posts"""
    nombre = models.CharField(max_length=60, unique=True)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.nombre

class PostTag(models.Model):
    """Modelo intermedio para relación muchos a muchos entre Post y Tag"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['post', 'tag']
        verbose_name = 'Tag de Post'
        verbose_name_plural = 'Tags de Posts'

class Recurso(models.Model):
    """Modelo para recursos adicionales de posts (enlaces, PDFs, etc.)"""
    TIPO_CHOICES = [
        ('link', 'Enlace'),
        ('pdf', 'PDF'),
        ('imagen', 'Imagen'),
        ('video', 'Video'),
    ]
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='recursos')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    titulo = models.CharField(max_length=200)
    url = models.URLField()
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
    
    def __str__(self):
        return f"{self.titulo} - {self.post.titulo}"

class Comentario(models.Model):
    """Modelo para comentarios en posts"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"Comentario de {self.nombre} en {self.post.titulo}"
