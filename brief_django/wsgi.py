"""
WSGI config for brief_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Startup code


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brief_django.settings')

application = get_wsgi_application()
