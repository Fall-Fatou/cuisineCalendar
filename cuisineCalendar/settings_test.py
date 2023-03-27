from .settings import *
from .keys import SECRET_KEY

SECRET_KEY = SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = ['testserver']


# Adding HTTPS and SSL
"""
# security.W016
CSRF_COOKIE_SECURE = True

# security.W012
SESSION_COOKIE_SECURE = True

# security.W008
SECURE_SSL_REDIRECT = True

# security.W005
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# security.W021
SECURE_HSTS_PRELOAD = True
"""

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mealPlanner',
    'accounts',
    # Only for test environment
    'Tests',
    # 'ratelimitbackend',
]

""" 
Configuration of rate limits for authentication.
"""
# Enable authentication rate limiting
AUTHENTICATION_RATELIMIT_ENABLE = True
# Set rate limits for login attempts to 5 per minute
AUTHENTICATION_RATELIMIT_LOGIN = '5/m'
# Set rate limits for registration attempts to 10 per minute
AUTHENTICATION_RATELIMIT_REGISTER = '10/m'
# Set rate limits for email verification attempts to 1 per 5 minutes
AUTHENTICATION_RATELIMIT_VERIFY_EMAIL = '1/5m'
# Block the user for 15 minutes after 5 failed login attempts
RATETIME_MINUTES = 15
# Prefix for the key used to store the number of attempts
RATELIMIT_KEY_PREFIX = 'auth'
# Use Django's default cache to store attempts
RATELIMIT_USE_CACHE = 'default'


# Use another database for tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mealplanner_test',
        'USER': 'root',
        'PASSWORD': 'AmadouSow1290521',
        'HOST': 'localhost',
    }
}

