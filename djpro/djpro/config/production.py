import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'm5o_f3rgt)_m1ihuqb*4k=)dcf&r+hb*oxms=ylm)-i$61fe)y'

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': ''
    }
}

# config for docker, replace LOCATION to your own config.
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
