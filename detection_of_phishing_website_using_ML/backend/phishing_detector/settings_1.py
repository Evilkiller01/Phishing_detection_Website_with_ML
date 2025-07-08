import os
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

SECRET_KEY = 'x2=_eo19(ho&3&7d(^o0&qke0157w+=gc_m6m#8x#1y(9*(whz'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1',
                 'localhost',]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'detector.apps.DetectorConfig',
    'detector',
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


ROOT_URLCONF = 'phishing_detector.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Make sure you have templates/index.html
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

WSGI_APPLICATION = 'phishing_detector.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Only enable if you're sure your site will always use HTTPS
SECURE_HSTS_SECONDS = 30 * 24 * 60 * 60 # 30 days (start with this)
SECURE_HSTS_PRELOAD = True  # Optional: for preload list submission
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Protect subdomains
SECURE_SSL_REDIRECT = False  # Redirect all HTTP to HTTPS
SESSION_COOKIE_SECURE = True  # Only send session cookies over HTTPS
CSRF_COOKIE_SECURE = True  # Only send CSRF cookies over HTTPS
# Security settings (only when DEBUG=False)
if not DEBUG:
    # HTTPS settings
    SECURE_SSL_REDIRECT = False
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_SECONDS = 0 # 30 days (start with this)
    SECURE_HSTS_PRELOAD = True  # Optional: for preload list submission
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Protect subdomains
    SECURE_SSL_REDIRECT = False # Redirect all HTTP to HTTPS
    
    # Cookie settings
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    
    # HSTS (strict HTTPS)
    SECURE_HSTS_SECONDS = 30 * 24 * 60 * 60
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    
    # Other security headers
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
