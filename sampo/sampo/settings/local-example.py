"""
local settings for sampo project.

"""

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
