from django.contrib import admin
from .models import Post, Categoria, Tag, PostTag, Recurso, Comentario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color']
    search_fields = ['nombre']
    list_filter = ['nombre']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1

class RecursoInline(admin.TabularInline):
    model = Recurso
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'estado', 'fecha_publicacion', 'likes', 'vistas']
    list_filter = ['estado', 'categoria', 'fecha_publicacion']
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ['fecha_actualizacion', 'vistas']
    inlines = [PostTagInline, RecursoInline]
    
    fieldsets = (
        ('Información básica', {
            'fields': ('titulo', 'slug', 'contenido', 'resumen', 'categoria')
        }),
        ('Imagen', {
            'fields': ('imagen_principal',)
        }),
        ('Estado y métricas', {
            'fields': ('estado', 'likes', 'vistas', 'fecha_publicacion', 'fecha_actualizacion')
        }),
    )

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'post', 'tipo', 'url']
    list_filter = ['tipo', 'post']
    search_fields = ['titulo', 'post__titulo']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'post', 'fecha_creacion', 'aprobado']
    list_filter = ['aprobado', 'fecha_creacion', 'post']
    search_fields = ['nombre', 'email', 'contenido']
    list_editable = ['aprobado']
    actions = ['aprobar_comentarios', 'rechazar_comentarios']
    
    def aprobar_comentarios(self, request, queryset):
        queryset.update(aprobado=True)
    aprobar_comentarios.short_description = "Aprobar comentarios seleccionados"
    
    def rechazar_comentarios(self, request, queryset):
        queryset.update(aprobado=False)
    rechazar_comentarios.short_description = "Rechazar comentarios seleccionados"
