"""
local settings for sampo project.

"""

# These must be set in production
DEBUG = False  # Or True if you are debugging something
SECRET_KEY = 'lajsdnfbalu7y4tou3jehgHGLj6GYU67(UI42#b*lfaahz_)n@'
#ALLOWED_HOSTS = ['sampocruises.com', 'www.sampocruises.com']
#STATIC_ROOT = '/site/sampocruises.com/www/static'
#MEDIA_ROOT = '/site/sampocruises.com/www/media'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sampo',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

LANGUAGE_CODE = 'fi-fi'
TIME_ZONE = 'Europe/Helsinki'

# Wagtail settings
WAGTAIL_SITE_NAME = "sampo"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
# BASE_URL = 'https://sampocruises.com'
BASE_URL = 'http://127.0.0.1:8000'
