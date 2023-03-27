from .settings import *
from cuisineCalendar.keys import SECRET_KEY

SECRET_KEY = SECRET_KEY

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

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
    'debug_toolbar',
]

# Configuration of Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
    'INTERCEPT_REDIRECTS': False,
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Only for dev environment
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'ratelimitbackend.middleware.RateLimitMiddleware',
]

# Update the database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mealplanner',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
    }
}


