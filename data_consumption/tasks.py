from celery import shared_task
from data_consumption.storage_movie import StorageMovie

@shared_task()
def get_popular_movie():
    st = StorageMovie()
    st.storage_movie_data()