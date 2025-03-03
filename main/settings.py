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

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


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
]

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
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

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
# ACCOUNT_EMAIL_REQUIRED = True

# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
# ACCOUNT_LOGIN_REDIRECT_URL = '/'

ACCOUNT_FORMS = {
    'signup': 'app.forms.CustomSignupForm',
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

from import_export.formats.base_formats import XLSX, XLS, CSV
IMPORT_EXPORT_FORMATS = [XLSX, XLS, CSV]

# ajax_datatable settings
AJAX_DATATABLE_MAX_COLUMNS = 30
AJAX_DATATABLE_TRACE_COLUMNDEFS = True
AJAX_DATATABLE_TRACE_QUERYDICT = True
AJAX_DATATABLE_TRACE_QUERYSET = True
AJAX_DATATABLE_TEST_FILTERS = True
AJAX_DATATABLE_DISABLE_QUERYSET_OPTIMIZATION = True