"""
Django settings for Text_app project.

Generated by 'django-admin startproject' using Django 4.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-797hk&vu1n5i_y)tf_43-+jserxbfr5mhhou52x#=7(%l^a_0q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'pdf_to_summary',
    'text',
    'grammar_correct',
    'history'
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

ROOT_URLCONF = 'Text_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
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

WSGI_APPLICATION = 'Text_app.wsgi.application'

# MEDIA_URL = '/static/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static')


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME':'text_appdb',
#     }
# }

DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'text_app',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'mongodb+srv://django:1234@cluster0.vldruo8.mongodb.net/?retryWrites=true&w=majority',
                # 'host': 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'

            }  
        }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'text_app',
#         'CLIENT': {
#             'host': os.environ.get('MONGO_URI', 'mongodb://admin:password@mongodb:27017/'),
#             'port': 27017,
#             'username': 'admin',
#             'password': 'password',
#             'authSource': 'admin',
#         }
#     }
# }

# DATABASES = {
# "default": {
#     "ENGINE": "djongo",
#     'ENFORCE_SCHEMA': False,
#     "NAME": "text_app",  # name of your DB which you want to access
#     "CLIENT": {
#         'host': 'mongodb+srv://django:1234@cluster0.vldruo8.mongodb.net/?retryWrites=true&w=majority',  # your db_url if not hosted then localhost
#         'port': 27017,  # port e.g. 27017
#         'username': 'django',
#         'password': '1234',
#          # set your db auth_source if you know
#         'authMechanism': 'SCRAM-SHA-1'  # set your auth_mechanism if you know
 
#     }
# }
# settings.py
AUTH_USER_MODEL = 'login.User'


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sampleuser788@gmail.com'
EMAIL_HOST_PASSWORD = 'vcdl vzmt ulbe hobq'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600
