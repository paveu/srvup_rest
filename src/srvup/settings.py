"""
Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import urlparse
import datetime
import dj_database_url
from django.core.urlresolvers import reverse
from billing.usdtopln import exchangeRateUSD
from .utils import jwt_response_payload_handler

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'accounts.MyUser'

# Application definition

INSTALLED_APPS = (
    'storages', # AWS S3 static media handler
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'django.contrib.admin',
    'django.contrib.auth',
    # https://docs.djangoproject.com/en/1.9/ref/contrib/contenttypes/
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'crispy_forms',
    'django.contrib.sites',
    # https://github.com/ottoyiu/django-cors-headers
    # http://www.html5rocks.com/en/tutorials/cors/
    # corsheaders does is not supported for django > 1.8
    'corsheaders',
    'rest_framework',
    'accounts',
    'billing',
    'analytics',
    'comments',
    'notifications',
    'videos',
    # allauth
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of 'allauth'
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware', #redis session caching
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # https://github.com/ottoyiu/django-cors-headers
    # http://www.html5rocks.com/en/tutorials/cors/
    # corsheaders does is not supported for django > 1.8
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',#redis session caching
)

ROOT_URLCONF = 'srvup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
       'DIRS': [os.path.join(BASE_DIR, "templates")],
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

WSGI_APPLICATION = 'srvup.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#from django.conf import settings
#from django.core.mail import send_mail
#send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
#         ['to@example.com'], fail_silently=False)


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

RECENT_COMMENT_NUMBER = 10

# Django-rest-framework-JWT for tokenzing an access to serializers
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': jwt_response_payload_handler,
    # token will live for 13h 55min
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=500000),
}

# https://github.com/ottoyiu/django-cors-headers
# A Django App that adds CORS (Cross-Origin Resource Sharing) headers to responses.
# Although JSON-P is useful, it is strictly limited to GET requests. 
# CORS builds on top of XmlHttpRequest to allow developers to make cross-domain 
# requests, similar to same-domain requests. Read more about it here: 
# http://www.html5rocks.com/en/tutorials/cors/ 
#
# CORS will be used in jQuery tests located in templates/jquery
# corsheaders does is not supported for django > 1.8

CORS_URLS_REGEX = r'^/api2/.*'
CORS_ORIGIN_ALLOW_ALL = True # any .net .com are allowed to access our domain
CORS_ORIGIN_WHITELIST = (
    'localhost',
)

# ALLAUTH SECTION
SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
LOGIN_REDIRECT_URL = "/"
SOCIALACCOUNT_EMAIL_VERIFICATION = True

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC':  lambda request: 'en_US',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v2.4'
       }}
# ACCOUNT_ADAPTER = 'accounts.adapter.MyAccountAdapter'

### PAYMENT PAYU SECTION
TEST_POS_ID = 145227
TEST_MD5_KEY = '12f071174cb7eb79d4aac5bc2f07563f'
TEST_SECOND_MD5_KEY = '13a980d4f851f3d9a1cfc792fb1f5e50'
AUTHORIZATION = '3e5cac39-7e38-4139-8fd6-30adc06a61bd'

# Your POS ID. If not provided the test payment value will be used.
PAYU_POS_ID = ''

# Your MD5 key. If not provided the test payment value will be used.
PAYU_MD5_KEY = ''

# Your second MD5 key. If not provided the test payment value will be used.
PAYU_SECOND_MD5_KEY = ''

# Payment validity time (in seconds), after which it's canceled, if user did not take action. If not provided 600 will be used.
PAYU_VALIDITY_TIME = 600

EXCHANGE_RATE = float(exchangeRateUSD()[2]) # sell price
UNIT_PRICE = 25 # USD
TOTAL_AMOUNT = int(UNIT_PRICE) * EXCHANGE_RATE

# braintree info
BRAINTREE_MERCHANT_ID = "v35fphbvqtvrp35k"
BRAINTREE_PUBLIC_KEY = "kkhkgx4bmkswv5yp"
BRAINTREE_PRIVATE_KEY = "7d8e596cb7ebe43e843ef95e9e068fa6"

def show_toolbar(request):
    if not request.is_ajax() and request.user and request.user.username == "paveu":
        return True
    return False


AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

if os.environ.get("CONFIG_ENV") == 'HEROKU' or os.environ.get("CONFIG_ENV") == 'AWS_ELASTIC_BEANSTALK':
    ## AWS S3 STATIC AND MEDIA HANDLER
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_REGION = 'eu-central-1' # FRANKFURT Endpoint: cp-media-static-bucket.s3-website.eu-central-1.amazonaws.com

    AWS_STORAGE_BUCKET_NAME = 'cp-media-static-bucket'
    AWS_S3_CALLING_FORMAT = "boto.s3.connection.OrdinaryCallingFormat"
    AWS_PRELOAD_METADATA = True
    
    if AWS_STORAGE_BUCKET_NAME:
        STATIC_URL = 'https://s3-%s.amazonaws.com/%s/static/' % (AWS_REGION, AWS_STORAGE_BUCKET_NAME)
        MEDIA_URL = 'https://s3-%s.amazonaws.com/%s/media/' % (AWS_REGION, AWS_STORAGE_BUCKET_NAME)
        STATICFILES_STORAGE = 'srvup.customstorages.StaticStorage'
        DEFAULT_FILE_STORAGE = 'srvup.customstorages.MediaStorage'
        STATICFILES_LOCATION = 'static'  # name of folder within bucket
        MEDIAFILES_LOCATION = 'media'    # name of folder within bucket
    else:
        STATIC_URL = '/static/'
        MEDIA_URL = '/media/'
    
    MEDIA_URL = os.environ.get('MEDIA_URL', MEDIA_URL)
    STATIC_URL = os.environ.get('STATIC_URL', STATIC_URL)
 
if os.environ.get("CONFIG_ENV") == 'AWS_ELASTIC_BEANSTALK':
    if 'RDS_DB_NAME' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAME'],
                'PORT': os.environ['RDS_PORT'],
            }
        } 


if os.environ.get("CONFIG_ENV") == 'HEROKU':
    #redis session caching
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
    
    # REDIS AND DATABASE SETTINGS FOR HEROKU
    redis_url = urlparse.urlparse(os.environ.get('REDIS_URL'))
    CACHES = {
        "default": {
             "BACKEND": "redis_cache.RedisCache",
             "LOCATION": "{0}:{1}".format(redis_url.hostname, redis_url.port),
             "OPTIONS": {
                 "PASSWORD": redis_url.password,
                 "DB": 0,
             }
        }
    }
    
    DATABASES = {
        'default': dj_database_url.config()
    }
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    FULL_DOMAIN_NAME = 'http://content-publisher-pro.herokuapp.com'

if os.environ.get("CONFIG_ENV") == 'local':
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': 'srvup.settings.show_toolbar'
    }

    # REDIS SESSION CACHING AND DATABASE SETTINGS FOR LOCAL DEV
    
    # CACHES = {
    #     'default': {
    #         'BACKEND': 'redis_cache.RedisCache',
    #         'LOCATION': '/var/run/redis/redis.sock',
    #     },
    # }
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    FULL_DOMAIN_NAME = 'https://content-publisher-pawelste.c9users.io/'
    
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")
    
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")


STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static_dirs"),
)