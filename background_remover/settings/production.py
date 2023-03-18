import os

from dotenv import load_dotenv

from background_remover.settings.common import *


# update envrionment variables for production
dotenv_path = os.path.join(BASE_DIR, ".env.production")
load_dotenv(dotenv_path)


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["PGDATABASE"],
        "USER": os.environ["PGUSER"],
        "PASSWORD": os.environ["PGPASSWORD"],
        "HOST": os.environ["PGHOST"],
        "PORT": os.environ["PGPORT"],
    }
}
