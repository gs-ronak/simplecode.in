from .base import *

#print('importing settings')

DEBUG = False

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

#INSTALLED_APPS += ["debug_toolbar", ]

#ALLOWED_HOSTS = ['localhost', ]

MIDDLEWARE_CLASSES += (
    'middleware.profile.ProfilerMiddleware',
)

PAGE_SIZE = 5
