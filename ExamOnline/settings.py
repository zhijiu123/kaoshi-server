"""
Django settings for ExamOnline project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%!t78vti6g=ejpbev3$45qjh)2)##eer9c=q#*71*+k0ynul!j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 解决拓展内置auth_user表出现的认证问题
# AUTH_USER_MODEL = 'user.Student'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'crispy_forms',
    'rest_framework',
    'django_filters',
    'import_export',
    'user',
    'exam',
    'question',
    'record'
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

ROOT_URLCONF = 'ExamOnline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'ExamOnline.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kaoshi',            # 数据库名
        'USER': 'root',     # MySQL 用户名
        'PASSWORD': '975891810', # MySQL 密码
        'HOST': '192.168.1.20',               # MySQL 主机地址
        'PORT': '3306',                    # MySQL 端口，默认为 3306
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
            'autocommit': True,
            'read_timeout': 3600,          # 设置读取超时时间
            'write_timeout': 3600,         # 设置写入超时时间
            'connect_timeout': 3600,       # 设置连接超时时间
        },
        'CONN_MAX_AGE': 600,  # 连接池中连接的最大寿命（以秒为单位），默认为 0（无限寿命）
    }
}

# redis配置
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://:975891810@192.168.1.22:6379',  # Redis服务器地址、端口号和密码
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# 使用Redis作为会话存储
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# restframework配置
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # Json Web Token
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    # restframework新版3.10.1需要指定默认schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# JWT设置
JWT_AUTH = {
    # token的有效期限
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # JWT跟前端保持一致，比如“token”这里设置成JWT
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    # 自定义方法返回用户信息
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.views.jwt_response_payload_handler'
}

EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 425
EMAIL_HOST_USER = "975891810@qq.com"
EMAIL_HOST_PASSWORD = "xzwhsnwtgstabbjh"  
EMAIL_USE_TLS= True
EMAIL_FROM = "975891810@qq.com"

