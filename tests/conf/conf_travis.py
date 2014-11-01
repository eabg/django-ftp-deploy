
SECRET_KEY = 'django-ftp-deploy'

ROOT_URLCONF = 'tests.conf.urls'

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

BROKER_URL = 'django://'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

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
    'crispy_forms',
    'braces',
    'django_nose',
    'django_coverage',
    'djcelery',
    'kombu.transport.django',
)

LOCAL_APPS = (
    'ftp_deploy',
    'ftp_deploy.server',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

DEFAULT_FILE_STORAGE = "inmemorystorage.InMemoryStorage"

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
