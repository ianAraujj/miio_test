import requests
import logging
from typing import Optional, Dict, Any, List, Union, Tuple, Callable, IO

# Setup logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

class TMDB(object):
    """
    Class for integration with The Movie db (TMDB) API
    """
    
    def __init__(self, token):
        
        # TOKEN
        self.token = token
        
        # URLS
        self.base_url = "https://api.themoviedb.org/3"
        self.file_base_url = "https://image.tmdb.org/t/p"
        self.popular_movies_url = f"{self.base_url}/movie/popular"
        self.list_genres_url = f"{self.base_url}/genre/movie/list"
        
        # HEADERS
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token),
        }

        
    def list_genres(self) -> Union[Dict, None]:
        """
        Get the list of official genres for movies.

        Returns:
            Union[Dict, None]: Dict or None
            
        Example:
            {
                "genres": [
                    {
                        "id": 28,
                        "name": "Action"
                    },
                ]
            }
        """
        r = requests.get(self.list_genres_url, headers=self.headers)
        
        try:
            return r.json()
        except Exception as e:
            logging.info(e)
            logging.error(f"Error list genres")
            return None
        
    def list_popular_movies(self) -> Union[Dict, None]:
        """
        Get a list of movies ordered by popularity.

        Returns:
            Union[Dict, None]: Dict or None
        """
        r = requests.get(self.popular_movies_url, headers=self.headers)
        
        try:
            return r.json()
        except Exception as e:
            logging.info(e)
            logging.error(f"Error popular movies")
            return None
            
    def download_file(self, filename: str, resolution: str) -> Union[IO, None]:
        """
        Download a file according to the information provided. 
        The file is retrieved through the TMDB API server.

        Returns:
            Union[Dict, None]: Dict or None
        """
        r = requests.get(f"{self.file_base_url}/{resolution}/{filename}", headers=self.headers)
        
        try:
            return r.content
        except Exception as e:
            logging.info(e)
            logging.error(f"Error download file")
            return None
            