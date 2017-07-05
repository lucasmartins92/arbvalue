import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '@_q8nxh#vo*bwhdqcm*$p0a&2@97flxed=x&nu4yld1ongspt)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['arbvalue.herokuapp.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'exchange',
    'storages',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
]

ROOT_URLCONF = 'arbvalue.urls'

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

WSGI_APPLICATION = 'arbvalue.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'levm2211',
        'HOST': '',
        'PORT': '',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#STATIC_URL = '/static/' #comentado para AWS S3 DJANGO-STORAGES
#MEDIA_URL = '/media/' #comentado para AWS S3 DJANGO-STORAGES

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "out_static", "static_root")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "our_static"),
)


MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "out_static", "media_root")


#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage' #comentado para AWS S3 DJANGO-STORAGES

AWS_HEADERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }
'''
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'arbvalue'
AWS_ACCESS_KEY_ID = 'AKIAJQMUXGQSOMOSPTWA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_HOST = 's3.us-east-2.amazonaws.com'

#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

S3_URL = 'http://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_DIRECTORY = '/static/'
MEDIA_DIRECTORY = '/media/'
STATIC_URL = S3_URL + STATIC_DIRECTORY
MEDIA_URL = S3_URL + MEDIA_DIRECTORY
'''

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
AWS_ACCESS_KEY_ID = 'AKIAJQMUXGQSOMOSPTWA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'arbvalue'
AWS_AUTO_CREATE_BUCKET = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
AWS_S3_CALLING_FORMAT = 'boto.s3.connection.OrdinaryCallingFormat'
AWS_S3_HOST = 's3.us-east-2.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_DIRECTORY = '/static/'
MEDIA_DIRECTORY = '/media/'
STATIC_URL = S3_URL + STATIC_DIRECTORY
MEDIA_URL = S3_URL + MEDIA_DIRECTORY


import dj_database_url
import djcelery
from datetime import timedelta

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
djcelery.setup_loader()
BROKER_URL = os.environ.get("REDISCLOUD_URL", "django://")
BROKER_POOL_LIMIT = 1
BROKER_CONNECTION_MAX_RETRIES = None
djcelery.setup_loader()
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json", "msgpack"]
CELERY_IMPORTS = ('exchange.tasks', )

CELERYBEAT_SCHEDULE = {
    'api-5sec': {
        'task': 'exchange.tasks.api',
        'schedule': timedelta(seconds=5),
        'args': ()
    },
}

if BROKER_URL == "django://":
    INSTALLED_APPS += ("kombu.transport.django",)