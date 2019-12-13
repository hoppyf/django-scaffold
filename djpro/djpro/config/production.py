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

# docker配置redis容器名为redis，其他情况修改为ip/域名
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
