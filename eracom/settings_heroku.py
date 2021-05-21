from .settings import *
import django_heroku

# IMPORTANT: to enable these settings in Heroku, set the corresponding environment variable using:

DEBUG = False

ALLOWED_HOSTS = ['eracom.herokuapp.com']
MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']
# Configure Django App for Heroku.
django_heroku.settings(locals())


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
