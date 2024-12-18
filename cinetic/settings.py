from pathlib import Path
from os import path, getenv
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(path.join('.env'))
SECRET_KEY = getenv("SECRET_KEY")
DATABASES = {
    'default': {
        'ENGINE': getenv("ENGINE"),
        'NAME': getenv("NAME"),
        'USER': getenv("USER"),
        'PASSWORD': getenv("PASSWORD"),
        'HOST': getenv("HOST"),
        'PORT': getenv("PORT"),
    }
}
DEBUG = getenv("DEBUG")
ALLOWED_HOSTS = [getenv("ALLOWED_HOST_1"), getenv("ALLOWED_HOST_2"), getenv("ALLOWED_HOST_3")]

INSTALLED_APPS = [
    'mainsite.apps.MainsiteConfig',
    'madishop.apps.MadishopConfig',
    # 'purbeurre.apps.PurbeurreConfig',
    'hunting_quizz.apps.HuntingQuizzConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'cinetic.urls'

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
        },
    },
]

WSGI_APPLICATION = 'cinetic.wsgi.application'

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

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
ATE_FORMAT = "d/m/Y"
USE_TZ = True

STATIC_ROOT = path.join(BASE_DIR, 'static/')
STATIC_URL = 'static/'

# Path for uploaded files on Django app
MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "madishop.Customer"
