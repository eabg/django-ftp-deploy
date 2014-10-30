
SECRET_KEY = 'django-ftp-deploy'

ROOT_URLCONF = 'tests.conf.urls'

STATIC_URL = '/static/'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'django_nose',
)

LOCAL_APPS = (
    'ftp_deploy',
    'ftp_deploy.server',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

INSTALLED_APPS = THIRD_PARTY_APPS + LOCAL_APPS + DJANGO_APPS

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

SOUTH_TESTS_MIGRATE = True
DEFAULT_FILE_STORAGE = "inmemorystorage.InMemoryStorage"

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'