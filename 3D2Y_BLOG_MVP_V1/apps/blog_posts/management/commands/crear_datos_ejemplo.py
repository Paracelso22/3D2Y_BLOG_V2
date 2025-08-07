from django.core.management.base import BaseCommand
from apps.blog_posts.models import Categoria, Post, Tag, PostTag

class Command(BaseCommand):
    help = 'Crea datos de ejemplo para el blog'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo...')
        
        # Crear categorías
        categorias = [
            {'nombre': 'Impresión 3D', 'descripcion': 'Todo sobre impresión 3D', 'color': '#FF6B35'},
            {'nombre': 'Tecnología', 'descripcion': 'Noticias y novedades tecnológicas', 'color': '#4ECDC4'},
            {'nombre': 'Tutoriales', 'descripcion': 'Guías paso a paso', 'color': '#45B7D1'},
            {'nombre': 'Reviews', 'descripcion': 'Reseñas de productos', 'color': '#96CEB4'},
        ]
        
        for cat_data in categorias:
            categoria, created = Categoria.objects.get_or_create(
                nombre=cat_data['nombre'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Categoría creada: {categoria.nombre}')
        
        # Crear tags
        tags = ['3D Printing', 'Tecnología', 'Tutorial', 'Review', 'Arduino', 'Raspberry Pi', 'Software']
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(nombre=tag_name)
            if created:
                self.stdout.write(f'Tag creado: {tag.nombre}')
        
        # Crear posts de ejemplo
        posts_data = [
            {
                'titulo': 'Mi Primera Impresión 3D',
                'contenido': '''
                <h2>Introducción a la Impresión 3D</h2>
                <p>La impresión 3D ha revolucionado la forma en que creamos objetos. En este post, te explico mi experiencia con mi primera impresora 3D.</p>
                
                <h3>¿Qué necesitas para empezar?</h3>
                <ul>
                    <li>Una impresora 3D (recomiendo la Ender 3 para principiantes)</li>
                    <li>Filamento PLA o PETG</li>
                    <li>Software de modelado 3D</li>
                    <li>Paciencia y ganas de aprender</li>
                </ul>
                
                <h3>Mi experiencia</h3>
                <p>Cuando recibí mi primera impresora 3D, estaba emocionado pero también nervioso. Después de configurar todo correctamente, mi primera impresión fue un éxito.</p>
                
                <h3>Consejos para principiantes</h3>
                <ol>
                    <li>Calibra tu impresora antes de cada impresión importante</li>
                    <li>Usa filamento de buena calidad</li>
                    <li>Mantén tu impresora limpia</li>
                    <li>No te desanimes si las primeras impresiones no salen perfectas</li>
                </ol>
                ''',
                'resumen': 'Experiencia personal con mi primera impresora 3D y consejos para principiantes.',
                'categoria': 'Impresión 3D',
                'estado': 'publicado',
                'tags': ['3D Printing', 'Tutorial']
            },
            {
                'titulo': 'Arduino vs Raspberry Pi: ¿Cuál elegir?',
                'contenido': '''
                <h2>Comparación: Arduino vs Raspberry Pi</h2>
                <p>Muchos se preguntan cuál es mejor para sus proyectos. La respuesta depende de lo que quieras hacer.</p>
                
                <h3>Arduino</h3>
                <p>Arduino es perfecto para:</p>
                <ul>
                    <li>Proyectos de automatización simple</li>
                    <li>Control de sensores y actuadores</li>
                    <li>Proyectos que requieren tiempo real</li>
                    <li>Aprendizaje de electrónica básica</li>
                </ul>
                
                <h3>Raspberry Pi</h3>
                <p>Raspberry Pi es ideal para:</p>
                <ul>
                    <li>Proyectos que requieren interfaz gráfica</li>
                    <li>Servidores web o aplicaciones</li>
                    <li>Procesamiento de datos complejos</li>
                    <li>Proyectos multimedia</li>
                </ul>
                
                <h3>Mi recomendación</h3>
                <p>Si eres principiante, empieza con Arduino. Si ya tienes experiencia, Raspberry Pi te abrirá más posibilidades.</p>
                ''',
                'resumen': 'Comparación detallada entre Arduino y Raspberry Pi para ayudarte a elegir el correcto para tu proyecto.',
                'categoria': 'Tecnología',
                'estado': 'publicado',
                'tags': ['Arduino', 'Raspberry Pi', 'Tecnología']
            },
            {
                'titulo': 'Review: Impresora 3D Ender 3 V2',
                'contenido': '''
                <h2>Review Completa: Ender 3 V2</h2>
                <p>Después de 6 meses usando la Ender 3 V2, aquí está mi opinión honesta.</p>
                
                <h3>Pros</h3>
                <ul>
                    <li>Excelente relación calidad-precio</li>
                    <li>Comunidad muy activa</li>
                    <li>Fácil de modificar y mejorar</li>
                    <li>Buena calidad de impresión</li>
                </ul>
                
                <h3>Contras</h3>
                <ul>
                    <li>Requiere calibración frecuente</li>
                    <li>El nivelado manual puede ser frustrante</li>
                    <li>Algunas piezas de menor calidad</li>
                </ul>
                
                <h3>Veredicto</h3>
                <p>Para su precio, es una excelente opción para principiantes y entusiastas. Recomendada 8/10.</p>
                ''',
                'resumen': 'Review detallada de la impresora 3D Ender 3 V2 después de 6 meses de uso.',
                'categoria': 'Reviews',
                'estado': 'publicado',
                'tags': ['3D Printing', 'Review']
            }
        ]
        
        for post_data in posts_data:
            categoria = Categoria.objects.get(nombre=post_data['categoria'])
            post, created = Post.objects.get_or_create(
                titulo=post_data['titulo'],
                defaults={
                    'contenido': post_data['contenido'],
                    'resumen': post_data['resumen'],
                    'categoria': categoria,
                    'estado': post_data['estado'],
                }
            )
            
            if created:
                # Agregar tags
                for tag_name in post_data['tags']:
                    tag = Tag.objects.get(nombre=tag_name)
                    PostTag.objects.get_or_create(post=post, tag=tag)
                
                self.stdout.write(f'Post creado: {post.titulo}')
        
        self.stdout.write(
            self.style.SUCCESS('¡Datos de ejemplo creados exitosamente!')
        )
