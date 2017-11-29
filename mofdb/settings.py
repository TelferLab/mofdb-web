"""
Django settings for mofdb project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from distutils.util import strtobool
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG_string = os.environ.get('DEBUG') or 'True'
DEBUG = bool(strtobool(DEBUG_string))

# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = '2t9+nz848gek0a4y54ts#)4q_%e7l!y2v*!!c_!cif1p6%=ws2'
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')


# ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = [
    'db',
    # 'dal',        # autocomplete-light
    # 'dal_select2',
    'grappelli',  # https://django-grappelli.readthedocs.io/en/latest/customization.html
    'grappelli_autocomplete_fk_edit_link',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django_extensions',  # https://github.com/django-extensions/django-extensions
    'django_cleanup',     # https://github.com/un1t/django-cleanup
    'rest_framework',
    'haystack',
    # Storages is used for S3 media storage.
    'storages',           # django-storages: https://github.com/jschneier/django-storages
    # 'django_tables2',     # https://github.com/bradleyayers/django-tables2
                          # 'nested_admin',       # https://github.com/theatlantic/django-nested-admin
    # 'debug_toolbar'      # django-debug-toolbar
    # 'livereload',
]

# Configure for bonsai in heroku: https://docs.bonsai.io/docs/django-haystack
from urllib.parse import urlparse
ES_URL = urlparse(os.environ.get('BONSAI_URL') or 'http://127.0.0.1:9200/')
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
        'URL': ES_URL.scheme + '://' + ES_URL.hostname + ':443',
        # 'URL': ES_URL.scheme + '://' + ES_URL.hostname + ':80',
        'INDEX_NAME': 'haystack',
    },
}
if ES_URL.username:
    HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": ES_URL.username + ':' + ES_URL.password}
# No management commands needed. Cons: Might provoke delay after save() models.
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mofdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.contrib.staticfiles.templatetags.staticfiles',
            ],
        },
    },
]

WSGI_APPLICATION = 'mofdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mofdb',
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mofdb',
    },
    # 'workbench': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'mofdb_v3',
    #     'USER': 'root',
    # },
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGIN_REDIRECT_URL = '/'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'] = dj_database_url.config(conn_max_age=500,
                                              # Local dev in db mofdb
                                              default='postgres:///mofdb')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*' ]
# ALLOWED_HOSTS = ['mofdb.herokuapp.com', '127.0.0.1' ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]
# swap order of defaults for grappelli
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'databasefiles')
MEDIA_URL = 'databasefiles/'

# Grappelli : https://django-grappelli.readthedocs.io/en/latest/customization.html
GRAPPELLI_ADMIN_TITLE = 'MoFDB Admin'

GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
    "db": {
        "baseligand": ("id__iexact", "name__icontains",),
        "ligand": ("id__iexact", "name__icontains",),
        "mof": ("id__iexact", "name__icontains",),
        "chemicalcompound": ("id__iexact", "name__icontains",),
        "datatype": ("id__iexact", "name__type",),
        "category": ("id__iexact", "name__icontains",),
        "functionalgroup": ("id__iexact", "name__icontains",),
        "reaction": ("id__iexact", "name__icontains",),
    }
}

# settings.py
## LOG everything (works in debug or in release)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mofdb.log',
            'formatter': 'verbose'
        },
       'console': {
           'level': 'DEBUG',
           'class': 'logging.StreamHandler',
          'formatter': 'verbose'
      }
    },
    'loggers': {
        'django': {
            'handlers':['file', 'console'],
            'propagate': True,
            'level':'DEBUG',
        },
        'db': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    }
}
