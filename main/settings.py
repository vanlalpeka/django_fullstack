"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from decouple import config


ADMINS = [('Admin', config('MY_EMAIL'))]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split()

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'app',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'invitations',
    "phonenumber_field",
    'import_export',
    'ajax_datatable',
    "django_bootstrap5",
]

# Session settings
SESSION_COOKIE_AGE = 60 * 60 * 1  # 1 hr
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # False to ensure the session persists even if the user closes their browser.
SESSION_SAVE_EVERY_REQUEST = True  # True to update the session age on every request.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.utils.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ["127.0.0.1"]

    
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": config("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": config("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": config("DB_USER", "user"),
        "PASSWORD": config("DB_PASSWORD", "password"),
        "HOST": config("DB_HOST", "localhost"),
        "PORT": config("DB_PORT", "5432"),
    }
}

# # Filesystem caching
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
#         "LOCATION": "/dev/shm/django_cache",
#         # "TIMEOUT": 60*5,
#         # "OPTIONS": {"MAX_ENTRIES": 1000},
#     }
# }

# SECURITY SETTINGS
if DEBUG:
    SECURE_SSL_REDIRECT=False
    SESSION_COOKIE_SECURE=False
    CSRF_COOKIE_SECURE=False

else:
    # sets the X-XSS-Protection: 1; mode=block header on all responses that do not already have it.
    # This header stops pages from loading when they detect reflected cross-site scripting (XSS) attacks.
    # This ensures third parties cannot inject scripts into your project.
    SECURE_BROWSER_XSS_FILTER = True

    # redirects all HTTP requests to HTTPS (unless exempt). 
    # If you have Nginx or Apache configured to do this already, this setting will be redundant.
    SECURE_SSL_REDIRECT = True  

    # tells the browser that cookies can only be handled over HTTPS
    SESSION_COOKIE_SECURE = True

    # same as SESSION_COOKIE_SECURE but applies to your CSRF token
    # ensures any forms submitted (for logins, signups, and so on) to the project were created by the project and not a third party.
    CSRF_COOKIE_SECURE = True

    # informs the browser that the project should only be accessed using HTTPS
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'  # Set to IST (Indian Standard Time)
USE_I18N = True  # Enable internationalization
USE_L10N = True  # Enable localization
USE_TZ = True    # Enable timezone support (recommended)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles' # In production, static files are served from this directory

# Base url to serve media files
MEDIA_URL = '/media/'
# Path where media is stored
MEDIA_ROOT = BASE_DIR / 'media'


FILE_UPLOAD_MAX_MEMORY_SIZE = 512000  # 500 kB
DATA_UPLOAD_MAX_MEMORY_SIZE = 512000  # 500 kB

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Authentication backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


# allauth settings
SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_LOGIN_METHODS = {"username"}
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = True

# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
# ACCOUNT_LOGIN_REDIRECT_URL = '/'

ACCOUNT_FORMS = {
    # 'signup': 'app.forms.CustomSignupForm',
    # 'login': 'app.forms.CustomLoginForm'
}

# # Settings for django-invitations
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config('MY_EMAIL')  # Replace with your email address
# EMAIL_HOST_PASSWORD = config('MY_EMAIL_PASSWORD')  # Replace with your email password
# DEFAULT_FROM_EMAIL = config('MY_EMAIL')   # Replace with your email address
# ACCOUNT_ADAPTER = 'invitations.models.InvitationsAdapter'
# INVITATIONS_ADAPTER = ACCOUNT_ADAPTER
# INVITATIONS_INVITATION_EXPIRY = 60  # days
# INVITATIONS_EMAIL_SUBJECT_PREFIX = 'Invitation to join'
# INVITATIONS_SIGNUP_REDIRECT = 'account_login'
# INVITATIONS_INVITATION_ONLY = True  # for allauth


# subclass AbstractUser
AUTH_USER_MODEL = 'app.CustomUser'

# import_export settings
IMPORT_EXPORT_SKIP_ADMIN_LOG=False
IMPORT_EXPORT_IMPORT_PERMISSION_CODE = "import"
IMPORT_EXPORT_EXPORT_PERMISSION_CODE = "export"

from import_export.formats.base_formats import XLSX, XLS, CSV
IMPORT_EXPORT_FORMATS = [XLSX, XLS, CSV]

# ajax_datatable settings
X_FRAME_OPTIONS = 'SAMEORIGIN'
AJAX_DATATABLE_MAX_COLUMNS = 30
AJAX_DATATABLE_TRACE_COLUMNDEFS = False
AJAX_DATATABLE_TRACE_QUERYDICT = False
AJAX_DATATABLE_TRACE_QUERYSET = False
AJAX_DATATABLE_TEST_FILTERS = False
AJAX_DATATABLE_DISABLE_QUERYSET_OPTIMIZATION = False
AJAX_DATATABLE_STRIP_HTML_TAGS = True


