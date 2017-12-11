"""
WSGI config for assisant project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assisant.settings")

application = get_wsgi_application()

sys.path.append('C:/Users/NightFly47/PycharmProjects/assisant')



