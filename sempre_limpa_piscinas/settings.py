# sempre_limpa_piscinas/settings.py

import os
from django.contrib.messages import constants
from pathlib import Path
from dotenv import load_dotenv
from corsheaders.defaults import default_headers

# Definição do diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Definição dos diretórios de templates e arquivos estáticos
TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'

# adicionar essa tag para que nosso projeto encontre o .env
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Configurações de segurança - Chave secreta e modo de debug
SECRET_KEY = os.getenv("SECRET_KEY")  # Nunca exponha em produção
DEBUG = os.getenv("DEBUG") == 'True'  # False em ambiente de produção

# [Configurações adicionais]

# Configurações de Produção (Descomente quando estiver em produção)
# --------------------------------------------------------------
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# DEBUG = False  # Lembre-se de desativar o DEBUG em produção

# Lista de hosts permitidos
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

CORS_ALLOWED_HEADERS = list(default_headers) + [
    'X-Register',
]

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    ADMINS = [(os.getenv('SUPER_USER'), os.getenv('EMAIL'))]
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# configuração CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Configurações de Aplicações Django instaladas
INSTALLED_APPS = [

    # Apps do projeto
    "accounts",

    # Apps do Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Apps de terceiros
    "corsheaders",

    # Apps do projeto
    "base",
    "myapp",
]

# Configurações de Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django_session_timeout.middleware.SessionTimeoutMiddleware',  # django-session-timeout
    "corsheaders.middleware.CorsMiddleware",  # corsheaders
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "requestlogs.middleware.RequestLogsMiddleware",
]

# Configurações de URL e WSGI
ROOT_URLCONF = "sempre_limpa_piscinas.urls"
WSGI_APPLICATION = "sempre_limpa_piscinas.wsgi.application"

# Configurações de Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR]
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # Apps
                "sempre_limpa_piscinas.context_processors.context_social",
            ],
        },
    },
]


# Configurações de Banco de Dados
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        'NAME': os.path.join(BASE_DIR, os.getenv('NAME_DB')),
        # 'USER':os.getenv('USER_DB')
        # 'PASSWORD': os.getenv('PASSWORD_DB')
        # 'HOST':os.getenv('HOST_DB')
        # 'PORT':os.getenv('PORT_DB')
    }
}

# Configurações de Framework REST
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'requestlogs.views.exception_handler',
}

# Configurações de Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'requestlogs_to_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'info.log',
        },
    },
    'loggers': {
        'requestlogs': {
            'handlers': ['requestlogs_to_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

REQUESTLOGS = {
    'SECRETS': ['password', 'token'],
    'METHODS': ('PUT', 'PATCH', 'POST', 'DELETE'),
}

# Configurações de validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Configurações de sessão e timeout
SESSION_EXPIRE_SECONDS = 1800  # 30 minutos
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True  # expira após o tempo de inatividade
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60  # 1 minuto
SESSION_TIMEOUT_REDIRECT = 'http://localhost:8000/'  # redireciona para a página de login

# Configurações de URL de login e logout
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Internationalization
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Configurações de arquivos estáticos e mídia
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Configuração do campo de chave primária padrão
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configurações de Email no Console (Comente para produção)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configurações de Email (Descomente e configure para produção)
# --------------------------------------------------------------
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
# DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
# SERVER_EMAIL = DEFAULT_FROM_EMAIL

# --- Messages --- #

MESSAGE_TAGS = {
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
    constants.DEBUG: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
}

