"""
Django settings for JonTomBraam project.
## Open shift credentials
  URL:        http://jontombraam-jontombraam.rhcloud.com/
  SSH to:     534d7c0550044603a3000497@jontombraam-jontombraam.rhcloud.com
  Git remote: ssh://534d7c0550044603a3000497@jontombraam-jontombraam.rhcloud.com/~/git/jontombraam.git/
  Cloned to:  /Users/wwhawkww/jontombraam
  Gears:          Located with python-2.7
  Connection URL: mysql://$OPENSHIFT_MYSQL_DB_HOST:$OPENSHIFT_MYSQL_DB_PORT/
  Database Name:  jontombraam
  Password:       QwLdEY7-Mxtm
  Username:       adminIj3qCSt
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9hxbvuoij3&cfxzy33920(fg3l&g@5#86%74kwszsoyt7cd*5f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
    )

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'JonTomBraam.urls'

WSGI_APPLICATION = 'JonTomBraam.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
  "default": {
      "ENGINE": 'django.db.backends.mysql',
      "NAME": "JonTomBraamdb",
      "USER": "root",
      "PASSWORD": "GXzO87MS",
      "HOST": "",
      "PORT": "",
  }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (os.path.join(BASE_DIR,'media') + '/',)
STATIC_ROOT = 'staticfiles'
STATIC_URL = os.path.join(BASE_DIR,'media') + '/'