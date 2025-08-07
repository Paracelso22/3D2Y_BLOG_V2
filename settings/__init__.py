"""
Settings package for my_3D2Y_blog project.
"""

import os

# Get the environment setting
DJANGO_ENVIRONMENT = os.environ.get('DJANGO_ENVIRONMENT', 'development')

if DJANGO_ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *
