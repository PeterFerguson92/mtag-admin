"""
Django settings for mtag_admin project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import environ
import sentry_sdk

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, "dev.env"))
print("USING " + env("ENVIROMENT") + " SETTINGS")
IS_DEV = env("ENVIROMENT") == "DEV"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-gyw&=2$1h(&^4+vm*0+7sw=*w#jdyaaqy%%r7w-+d70x@k-)zg'
with open(os.path.join(BASE_DIR, "secret_key.txt")) as f:
    SECRET_KEY = f.read().strip()
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("ENABLE_DEBUG") == "True"
if IS_DEV:
    ALLOWED_HOSTS = ["localhost"]
else:
    ALLOWED_HOSTS = [env("ALLOWED_HOST"), "localhost"]
    CSRF_TRUSTED_ORIGINS = [env("CSRF_TRUSTED_ORIGIN")]

# Application definition

INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    "daterange.apps.DateRangeFilterConfig",
    "rest_framework",
    "reset_migrations",
    "corsheaders",
    "import_export",
    "activities",
    "ministries",
    "homepage",
    "servicemanagement",
    "finance"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ORIGIN_WHITELIST = (
    "http://localhost:4200",
    "https://mtag-admin-production.up.railway.app",
)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "https://mtag-admin-production.up.railway.app",
]
CORS_ALLOW_ALL = False

ROOT_URLCONF = "mtag_admin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mtag_admin.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if IS_DEV:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("PGDATABASE"),
            "USER": env("PGUSER"),
            "PASSWORD": env("PGPASSWORD"),
            "HOST": env("PGHOST"),
            "PORT": env("PGPORT"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


USE_S3 = os.getenv("USE_S3") == "FALSE"

CORS_ORIGIN_ALLOW_ALL = True

STATIC_URL = "/static/"
# Extra places for collectstatic to find static files.
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = ("admin", os.path.join(BASE_DIR, "static", "admin"))

MEDIA_URL = "/media/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
AWS_S3_SIGNATURE_NAME = ("s3v4",)
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATE_FORMAT = "d-m-Y"
DATE_INPUT_FORMATS = (("%d-%m-%Y"),)

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Belfast"

USE_I18N = True

USE_L10N = False

USE_TZ = False

X_FRAME_OPTIONS = "SAMEORIGIN"

XS_SHARING_ALLOWED_METHODS = ["POST", "GET", "OPTIONS", "PUT", "DELETE"]

STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")


sentry_sdk.init(
    dsn="https://04e21e4909b4eec7dce1bbe8953f575a@o4505039653896192.ingest.sentry.io/4506713537052672",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)