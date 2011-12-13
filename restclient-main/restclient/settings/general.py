import os

ENVIRONMENT = 'prod'

# Django settings for restclient project.

SITE_ID = 1
DEFAULT_CHARSET = "utf8"
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

USE_I18N = True

MEDIA_ROOT = ''

MEDIA_URL = "http://onlinerestclient.appspot.com/static/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b!j@0verw&n(9+(+&=_+yamxg=uh(tkbs=9ban2^05ui6w2pt!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    'gaesessions.DjangoSessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'restclient.urls'

ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, os.pardir,'templates').replace('\\','/'),
    os.path.join(ROOT_PATH, os.pardir,'templates/root').replace('\\','/')
)

INSTALLED_APPS = ()
