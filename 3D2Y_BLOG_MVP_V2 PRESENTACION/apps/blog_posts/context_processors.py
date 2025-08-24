from .models import Categoria

def categorias_globales(request):
    """Context processor para proporcionar categorías a todos los templates"""
    return {
        'categorias': Categoria.objects.all()
    }
