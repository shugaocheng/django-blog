"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k+2%53g_o$_i&_7qhtw^yt(n60ez-mi(4zp_r51i^sn24zlc6v'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 站点ID
SITE_ID = 1
# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',             # 管理站点框架
    'django.contrib.auth',              # 权限框架
    'django.contrib.contenttypes',      # 内容类型框架
    'django.contrib.sessions',          # 会话框架
    'django.contrib.messages',          # 消息框架
    'django.contrib.staticfiles',       # 管理静态文件的框架
    'blog',
    'django_pdb',
    # 标签应用
    'taggit',
    'django.contrib.sites',             #
    'django.contrib.sitemaps',          # 站点地图
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',   # 更改admin站点语言显示

)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# 邮箱配置:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.163.com' #SMTP服务器
EMAIL_PORT = 25           #SMTP端口
EMAIL_HOST_USER = 'shugaocheng@163.com' #用该邮箱发邮件，邮箱必须有效
EMAIL_HOST_PASSWORD = 'wp1993524'  #邮箱密码，必须正确
EMAIL_USE_TLS = True           #与SMTP服务器通信时，是否启动TLS连接（安全连接），默认为false
EMAIL_TO_RECEIPT = ['shugaocheng@163.com','70016803@qq.com']


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        'NAME': 'my_blog',
        'USER': 'root',
        'PASSWORD': 'wp1993524.',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us' # 默认语言编码

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
