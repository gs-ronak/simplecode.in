"""
WSGI config for django_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

#import os
# from os.path import abspath, dirname
# from sys import path

# SITE_ROOT = dirname(dirname(abspath(__file__)))
# path.append(SITE_ROOT)

# print('Project name ==> {{ project_name }}')

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings.dev")

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()


# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.dev")
# application = get_wsgi_application()
import os
from os.path import abspath, dirname
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
#print(SITE_ROOT)
#print(path)

path.append(SITE_ROOT)

#print(path)
# print('Project name ==> {{ project_name }}')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings.dev")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
