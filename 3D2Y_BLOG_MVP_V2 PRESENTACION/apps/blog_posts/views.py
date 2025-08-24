from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Categoria, Tag, Comentario

def home(request):
    """Vista para la página de inicio"""
    # Obtener posts destacados (los más recientes publicados)
    posts_destacados = Post.objects.filter(estado='publicado').order_by('-fecha_publicacion')[:5]
    categorias = Categoria.objects.all()
    
    context = {
        'title': 'Inicio - 3D2Y Blog',
        'hero_title': 'Bienvenido a 3D2Y Blog',
        'hero_subtitle': 'Descubre el mundo de la impresión 3D y la tecnología',
        'posts_destacados': posts_destacados,
        'categorias': categorias,
    }
    return render(request, 'blog_posts/home.html', context)

def blog_list(request):
    """Vista para listar todas las publicaciones del blog"""
    posts = Post.objects.filter(estado='publicado').order_by('-fecha_publicacion')
    categorias = Categoria.objects.all()
    
    context = {
        'title': 'Blog - 3D2Y Blog',
        'posts': posts,
        'categorias': categorias,
    }
    return render(request, 'blog_posts/blog_list.html', context)

def blog_detail(request, slug):
    """Vista para mostrar una publicación específica"""
    post = get_object_or_404(Post, slug=slug, estado='publicado')
    
    # Incrementar vistas
    post.vistas += 1
    post.save()
    
    # Obtener comentarios aprobados
    comentarios = post.comentarios.filter(aprobado=True)
    
    context = {
        'title': f'{post.titulo} - 3D2Y Blog',
        'post': post,
        'comentarios': comentarios,
    }
    return render(request, 'blog_posts/blog_detail.html', context)

def posts_por_categoria(request, categoria_id):
    """Vista para mostrar posts de una categoría específica"""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = Post.objects.filter(categoria=categoria, estado='publicado').order_by('-fecha_publicacion')
    
    context = {
        'title': f'Posts de {categoria.nombre} - 3D2Y Blog',
        'categoria': categoria,
        'posts': posts,
    }
    return render(request, 'blog_posts/posts_por_categoria.html', context)

def about(request):
    """Vista para la página Acerca de"""
    context = {
        'title': 'Acerca de - 3D2Y Blog',
    }
    return render(request, 'blog_posts/about.html', context)

def contact(request):
    """Vista para la página de contacto"""
    context = {
        'title': 'Contacto - 3D2Y Blog',
    }
    return render(request, 'blog_posts/contact.html', context)

def search_posts(request):
    """Vista para buscar posts"""
    query = request.GET.get('q', '').strip()
    posts = []
    
    if query:
        # Búsqueda en título y contenido
        from django.db.models import Q
        posts = Post.objects.filter(
            Q(titulo__icontains=query) | 
            Q(contenido__icontains=query),
            estado='publicado'
        ).order_by('-fecha_publicacion')
    
    context = {
        'title': f'Búsqueda: {query} - 3D2Y Blog',
        'query': query,
        'posts': posts,
        'total_results': len(posts) if posts else 0,
    }
    return render(request, 'blog_posts/search_results.html', context)

# Vistas protegidas para administradores
@login_required
def admin_dashboard(request):
    """Dashboard para administradores"""
    total_posts = Post.objects.count()
    posts_publicados = Post.objects.filter(estado='publicado').count()
    posts_borrador = Post.objects.filter(estado='borrador').count()
    total_categorias = Categoria.objects.count()
    
    context = {
        'title': 'Dashboard - 3D2Y Blog',
        'total_posts': total_posts,
        'posts_publicados': posts_publicados,
        'posts_borrador': posts_borrador,
        'total_categorias': total_categorias,
    }
    return render(request, 'blog_posts/admin_dashboard.html', context)

@login_required
def quick_post_create(request):
    """Vista rápida para crear posts con validación mejorada"""
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        contenido = request.POST.get('contenido', '').strip()
        categoria_id = request.POST.get('categoria')
        
        # Validación mejorada
        errors = []
        
        if not titulo:
            errors.append('El título es obligatorio.')
        elif len(titulo) < 5:
            errors.append('El título debe tener al menos 5 caracteres.')
        elif len(titulo) > 200:
            errors.append('El título no puede exceder 200 caracteres.')
            
        if not contenido:
            errors.append('El contenido es obligatorio.')
        elif len(contenido) < 50:
            errors.append('El contenido debe tener al menos 50 caracteres.')
        elif len(contenido) > 10000:
            errors.append('El contenido no puede exceder 10,000 caracteres.')
        
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            try:
                categoria = None
                if categoria_id:
                    categoria = Categoria.objects.get(id=categoria_id)
                
                # Crear slug automático basado en el título
                from django.utils.text import slugify
                from django.db import IntegrityError
                
                base_slug = slugify(titulo)
                slug = base_slug
                counter = 1
                
                # Verificar si el slug ya existe
                while Post.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                
                post = Post.objects.create(
                    titulo=titulo,
                    contenido=contenido,
                    categoria=categoria,
                    slug=slug,
                    estado='publicado',
                    autor=request.user
                )
                
                messages.success(request, f'Post "{post.titulo}" creado exitosamente.')
                return redirect('blog_posts:admin_dashboard')
                
            except IntegrityError:
                messages.error(request, 'Error al crear el post. Inténtalo de nuevo.')
            except Exception as e:
                messages.error(request, f'Error inesperado: {str(e)}')
    
    categorias = Categoria.objects.all()
    context = {
        'title': 'Crear Post - 3D2Y Blog',
        'categorias': categorias,
    }
    return render(request, 'blog_posts/quick_post_create.html', context)

def agregar_comentario(request, post_id):
    """Vista para agregar comentarios a un post"""
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id, estado='publicado')
        
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip()
        contenido = request.POST.get('contenido', '').strip()
        
        # Validación básica
        if not nombre or not email or not contenido:
            messages.error(request, 'Por favor completa todos los campos.')
        elif len(contenido) < 10:
            messages.error(request, 'El comentario debe tener al menos 10 caracteres.')
        elif len(contenido) > 1000:
            messages.error(request, 'El comentario no puede exceder 1000 caracteres.')
        else:
            try:
                comentario = Comentario.objects.create(
                    post=post,
                    nombre=nombre,
                    email=email,
                    contenido=contenido,
                    aprobado=False  # Los comentarios requieren aprobación
                )
                messages.success(request, 'Tu comentario ha sido enviado y está pendiente de aprobación.')
            except Exception as e:
                messages.error(request, 'Error al enviar el comentario. Inténtalo de nuevo.')
        
        return redirect('blog_posts:blog_detail', slug=post.slug)
    
    return redirect('blog_posts:home')

@login_required
def manage_posts(request):
    """Vista temporal para gestionar posts"""
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        action = request.POST.get('action')
        
        if post_id and action:
            try:
                post = Post.objects.get(id=post_id)
                if action == 'publish':
                    post.estado = 'publicado'
                    post.save()
                    messages.success(request, f'Post "{post.titulo}" publicado exitosamente.')
                elif action == 'unpublish':
                    post.estado = 'borrador'
                    post.save()
                    messages.success(request, f'Post "{post.titulo}" movido a borradores.')
                elif action == 'delete':
                    post.delete()
                    messages.success(request, f'Post "{post.titulo}" eliminado exitosamente.')
            except Post.DoesNotExist:
                messages.error(request, 'Post no encontrado.')
    
    posts = Post.objects.all().order_by('-fecha_publicacion')
    context = {
        'title': 'Gestionar Posts - 3D2Y Blog',
        'posts': posts,
    }
    return render(request, 'blog_posts/manage_posts.html', context)
