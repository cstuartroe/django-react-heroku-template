import os
from django.core.management.utils import get_random_secret_key

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'django-react-heroku-template.herokuapp.com',
]

DEBUG = bool(os.getenv('DEBUG'))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'dist'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SECRET_KEY = get_random_secret_key()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_react_heroku_template.apps.DjangoHerokuReactTemplateConfig',
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

ROOT_URLCONF = 'django_react_heroku_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': ['django.templatetags.static']
        },
    },
]

WSGI_APPLICATION = 'django_react_heroku_template.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DEV_SQLITE = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': "db.sqlite3",
}

PROD_PG = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.getenv("PG_DB"),
    'USER': os.getenv("PG_USER"),
    'PASSWORD': os.getenv("PG_PASSWORD"),
    'HOST': os.getenv("PG_HOST"),
    'PORT': '5432',
}

USE_DEV = bool(os.getenv("USE_DEV"))

DATABASES = {
    'default': DEV_SQLITE if USE_DEV else PROD_PG
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = 'static/'
