from decouple import config
from dj_database_url import parse as parse_db_url

DEBUG = False

DATABASES = {
    'default': config(
        'DATABASE_URL',
        cast=parse_db_url
    ),
}