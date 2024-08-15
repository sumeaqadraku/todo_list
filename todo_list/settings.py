# Importing the Path class for file system path operations
from pathlib import Path

# Setting the base directory of the project (two levels up from this settings file)
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - for non-production use
SECRET_KEY = 'django-insecure-u0uth%z9p0y%(f8=*fm+s-sz3+i0(qj@hdf@8b!pt(+cmw^vhg'  # Secret key for cryptographic operations

DEBUG = True  # Debug mode enabled, not for production

ALLOWED_HOSTS = []  # Hosts allowed to serve the app. Empty for now (localhost only).

# Installed apps include default Django apps (admin, auth, etc.) and the custom app `base`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',  # The custom app named `base`
]

# Middleware is used to process requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration pointing to 'todo_list.urls' which handles the URL routing
ROOT_URLCONF = 'todo_list.urls'

# Template settings, used to render HTML files
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # List of directories to search for templates
        'APP_DIRS': True,  # Looks for templates inside installed apps
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

# WSGI configuration, used to deploy the project with WSGI servers
WSGI_APPLICATION = 'todo_list.wsgi.application'

# Database configuration - using SQLite by default
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Database file stored in the BASE_DIR
    }
}

# Password validation rules to enforce stronger password policies
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

# Internationalization and localization settings
LANGUAGE_CODE = 'en-us'  # Default language is English (US)
TIME_ZONE = 'UTC'  # Default timezone is UTC
USE_I18N = True  # Enable Django's translation system
USE_TZ = True  # Enable timezone support

# Static files settings (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
