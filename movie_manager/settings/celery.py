from decouple import config
from celery.schedules import crontab

# Celery settings
CELERY_BROKER_URL = config('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = config('CELERY_BROKER_URL')
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BEAT_SCHEDULE = {
    'get_popular_movie': {
        'task': 'data_consumption.get_popular_movie',
        'schedule': crontab(minute=0, hour='*/2')
    },
}

#CELERY_TIMEZONE = 'America/Fortaleza'
#CELERY_TIMEZONE = 'UTC'
#CELERY_ENABLE_UTC = True
#CELERY_ACCEPT_CONTENT = ['json']
#CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'