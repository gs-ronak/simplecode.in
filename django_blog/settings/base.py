# -*- coding: utf-8 -*-

# from os.path import abspath, basename, dirname, join
import os


# BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# BASE_DIR = dirname(dirname(abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# BASE_DIR = os.path.dirname( os.path.dirname(os.path.abspath(__file__)))


#print(BASE_DIR)
SECRET_KEY = 'xhcg42=d%md&1jcy$c8%#p5e+59!)25v$m$%uq*^1hfx%23i+p'
DEBUG = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = ''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'apps.blog',
    'apps.wedding',
    'pagedown',
    'compressor',
    # 'analytical',
]

SITE_ID = 1
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

ROOT_URLCONF = 'django_blog.urls'

WSGI_APPLICATION = 'django_blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = False

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-73612812-1'
GOOGLE_ANALYTICS_SITE_SPEED = True