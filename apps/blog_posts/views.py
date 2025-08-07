from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Categoria, Tag

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
    
    context = {
        'title': f'{post.titulo} - 3D2Y Blog',
        'post': post,
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
    """Vista rápida para crear posts"""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        categoria_id = request.POST.get('categoria')
        
        if titulo and contenido:
            categoria = None
            if categoria_id:
                categoria = Categoria.objects.get(id=categoria_id)
            
            post = Post.objects.create(
                titulo=titulo,
                contenido=contenido,
                categoria=categoria,
                estado='publicado'  # Cambiado de 'borrador' a 'publicado'
            )
            messages.success(request, f'Post "{post.titulo}" creado exitosamente.')
            return redirect('blog_posts:admin_dashboard')
        else:
            messages.error(request, 'Por favor completa todos los campos requeridos.')
    
    categorias = Categoria.objects.all()
    context = {
        'title': 'Crear Post - 3D2Y Blog',
        'categorias': categorias,
    }
    return render(request, 'blog_posts/quick_post_create.html', context)

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
