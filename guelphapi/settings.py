# Django settings for guelphapi project.

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, '../static_root')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'vwe!r#uv%f3))n^gk208kc1n-wxb7zl_tat^olf)q6x35f&amp;vc1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'guelphapi.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'guelphapi.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'guelphapi.api',
    'tastypie',
    'gunicorn',
    'kombu.transport.django',
    'djcelery',
    'mixpanel',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Custom Settings Here
NEWS_FEED_URL = 'http://feeds.feedburner.com/uoguelph'
EVENTS_FEED_URL = 'http://www.uoguelph.ca/studentaffairs/reg/rssfeed.cfm'

# To fetch course information
# COURSE_PROGRAM_ROOT_URL % COURSE_PROGRAM_CODES[i] = Full URL, where i is the program
COURSE_PROGRAM_ROOT_URL = 'http://www.uoguelph.ca/registrar/calendars/undergraduate/current/c12/c12%s.shtml'
COURSE_PROGRAM_CODES = (
    'acct', 'agr', 'anat', 'ansc', 'anth', 'arth', 'asci',
    'bioc', 'biol', 'biom', 'bot', 'bus',
    'chem', 'chin', 'clas', 'cis', 'coop', 'crop',
    'econ', 'edrd', 'engg', 'engl', 'envb', 'envm', 'envs', 'eqn', 'euro',
    'frhd', 'food', 'fare', 'fren',
    'geog', 'germ', 'grek',
    'hisp', 'hist', 'hk', 'hort', 'hrob', 'htm', 'humn',
    'ips', 'iss', 'univ', 'ibio', 'idev', 'ital',
    'larc', 'lat', 'ling',
    'mgmt', 'cost', 'math', 'mcb', 'micr', 'mbg', 'musc',
    'nano', 'neur', 'nrs', 'nutr',
    'oagr',
    'path', 'phrm', 'phil', 'port', 'phys', 'psgy', 'pbio', 'pols', 'popm', 'psyc',
    'real',
    'soc', 'soan', 'stat', 'sart',
    'thst', 'tox',
    'vetm',
    'wmst',
    'zoo',
)

BROKER_BACKEND = 'django'
CELERY_ALWAYS_EAGER = True
MIXPANEL_API_TOKEN = '29a29954d34fd707f1118f09b6b64a8f'

import djcelery
djcelery.setup_loader()

# Try to import our local settings (for database, etc)
# DO NOT remove this
try:
    from local_settings import *
except ImportError:
    pass
