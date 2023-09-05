from os import getenv
from os.path import join
from pathlib import Path

from django.urls import reverse_lazy


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv('SECRET_KEY')

DEBUG = getenv('DEBUG', False)

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', '').split()

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql",
		"NAME": getenv('DB_NAME'),
		"USER": getenv("DB_USER"),
		"PASSWORD": getenv("DB_PASSWORD"),
		"HOST": getenv('DB_HOST'),
		"PORT": getenv('DB_PORT'),
	}
}

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'to_deploy.app',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'to_deploy.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates']
		,
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'to_deploy.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
	# {
	# 	'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	# },
	# {
	# 	'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	# },
	# {
	# 	'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	# },
	# {
	# 	'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	# },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = 'static/'

STATICFILES_DIRS = [
	join(BASE_DIR, 'static_files'),
]

STATIC_ROOT = getenv('STATIC_ROOT', join(BASE_DIR, 'static'))

LOGIN_URL = reverse_lazy('login_user')

LOGIN_REDIRECT_URL = reverse_lazy('home')
