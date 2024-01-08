from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_qq7hj_qy1#4$gcz(eru@161(dws3!zi_m-t5-+f!n4&b+rl$&"

# Application definition
INSTALLED_APPS = [
    "db"
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

USE_TZ = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
