from django.urls import path
from . import views

app_name = 'blog_posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('categoria/<int:categoria_id>/', views.posts_por_categoria, name='posts_por_categoria'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_posts, name='search_posts'),
    path('post/<int:post_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
    
    # URLs protegidas para administradores
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('quick-create/', views.quick_post_create, name='quick_post_create'),
    path('manage-posts/', views.manage_posts, name='manage_posts'),
]
