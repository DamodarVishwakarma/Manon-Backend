"""
Django settings for ManOn_backend project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4v@f**$k3vs%ot5itbdg@_z2+0@8qszgwz-cw@o5ltc@&n-5s='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_data',
    'rest_framework',
    'rest_framework_simplejwt',
    'game',
    'celery',
    'django_celery_beat',
    'django_celery_results',
]

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

ROOT_URLCONF = 'ManOn_backend.urls'

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

WSGI_APPLICATION = 'ManOn_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': BASE_DIR / 'db.sqlite3',
#
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('DATABASE_NAME'),
#         'USER': os.environ.get('DATABASE_USER'),
#         'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
#         'HOST': os.environ.get('DATABASE_HOST'),
#         'PORT': os.environ.get('DATABASE_PORT'),
#     }
# }

# #
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'testdb',
#         'USER': 'vikrant',
#         'PASSWORD': 'vikrant123',
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'df2iahq3ass73a',
        'USER': 'shkxeyfiogduaf',
        'PASSWORD': '8043a2a2d2c7bd1398978d4416a9358e31be55e1653d169c2817afebb95d5658',
        'HOST': 'ec2-34-206-148-196.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user_data.UserTable'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
}

# EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')UTC
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
# EMAIL_PORT = os.environ.get('EMAIL_PORT')
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'lcy06shukla@gmail.com'
EMAIL_HOST_PASSWORD = 'rzstwzpghyosfozf'

# CELERY_RESULT_BACKEND = 'django-db'
# # CELERY_RESULT_BACKEND = 'db+sqlite:///results.db'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CELERY_CACHE_BACKEND = 'django-cache'


BROKER_URL = 'pyamqp://localhost'
CELERY_RESULT_BACKEND = 'rpc://localhost'
# Celery Data Format
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
