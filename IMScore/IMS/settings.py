"""
Django settings for IMS project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default="", cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',
    'django_filters',
    'widget_tweaks',
    'dbbackup',
    'martor',
    'intelsAPI',
    'frontend'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'IMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DB_NAME = os.getenv('POSTGRES_DB')
DB_USERNAME = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('DATABASE_HOST')
DB_PORT = os.getenv('DATABASE_PORT')


DATABASE_TYPE = config('DATABASE_TYPE')
if DATABASE_TYPE == 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif DATABASE_TYPE == 'postgres':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_NAME,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }
else:
    raise NotImplementedError('No database configuration for '+DATABASE_TYPE)


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = config("STATIC_ROOT")

MEDIA_URL = "/media/"
MEDIA_ROOT = config("MEDIA_ROOT")

SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', cast=bool)
SESSION_COOKIE_AGE = 2*3600
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', cast=bool)
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", cast=bool)
SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", cast=int, default=0)
SECURE_HSTS_INCLUDE_SUBDOMAINS= config("SECURE_HSTS_INCLUDE_SUBDOMAINS", cast=bool)


ADMINS = [(config('ADMIN_NAME'), config('ADMIN_EMAIL'))]
SERVER_EMAIL = config("SERVER_EMAIL")
DEFAULT_FROM_EMAIL = config("SERVER_EMAIL")

### Email - Start
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_TIMEOUT = config('EMAIL_TIMEOUT', cast=int)
### Email - End


#### Authentication - Start
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'search'
LOGOUT_REDIRECT_URL = LOGIN_URL
#### Authentication - End


### DRF - Start
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
}
### DRF - End


### Backup - Start
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'location': config('DBBACKUP_STORAGE_LOCATION'),
    'file_permissions_mode': 400,
    'directory_permissions_mode': 700
}
DBBACKUP_CLEANUP_KEEP = config('DBBACKUP_CLEANUP_KEEP', cast=int)
DBBACKUP_CLEANUP_KEEP_MEDIA = config('DBBACKUP_CLEANUP_KEEP', cast=int)
DBBACKUP_SEND_EMAIL = config('DBBACKUP_SEND_EMAIL', cast=bool)
DBBACKUP_FILENAME_TEMPLATE = 'db-{databasename}-{servername}-{datetime}.{extension}'
DBBACKUP_MEDIA_FILENAME_TEMPLATE = 'media-{servername}-{datetime}.{extension}'
DBBACKUP_GPG_ALWAYS_TRUST = config('DBBACKUP_GPG_ALWAYS_TRUST', cast=bool)
DBBACKUP_GPG_RECIPIENT = config('ADMIN_EMAIL')
DBBACKUP_GPG_PASSPHRASE = config('DBBACKUP_GPG_PASSPHRASE')  # custom
### Backup - End


### Martor - Start
# Martor Configuration
MARTOR_THEME = 'bootstrap'  # semantic
MARTOR_ENABLE_LABEL = True
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'false',
    'imgur': 'false',        # to enable/disable imgur/custom uploader.
    'mention': 'false',      # to enable/disable mention
    'jquery': 'false',       # to include/revoke jquery (require for admin default django)
    'living': 'false',      # to enable/disable live updates in preview
    'spellcheck': 'true',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',         # to enable/disable hljs highlighting in preview
}
MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'image-upload',
    'direct-mention', 'toggle-maximize', 'help'
]

MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',
    'markdown.extensions.toc',

    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins',      # ~~strikethrough~~ and ++underscores++
    'martor.extensions.escape_html',  # to handle the XSS vulnerabilities
]
### Martor - End


