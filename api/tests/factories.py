import factory
import random
import base64
from io import BytesIO
from PIL import Image
from core.models.movie import Movie
from core.models.genre import Genre

class GenreFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Genre
        
    name = factory.Faker('word')
    
class MovieFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Movie
    
    adult = factory.LazyAttribute(
        lambda o: random.choice([True, False])
    )
    original_language = 'en'
    original_title = factory.Faker('sentence', nb_words=3)
    title = factory.Faker('sentence', nb_words=3)
    overview = factory.Faker('text')
    release_date = factory.Faker('date')
    popularity = factory.Faker('pydecimal', min_value=0, max_value=20000, left_digits=5, right_digits=4)
    vote_average = factory.Faker('pydecimal', min_value=0, max_value=10, left_digits=2, right_digits=1)
    vote_count = factory.Faker('pyint', min_value=0)
    backdrop_path = None
    poster_path = None
    
    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            # If the instance has not been created, do not add genres
            return
        
        if extracted:
            # Add the explicitly passed genres
            for genre in extracted:
                self.genres.add(genre)
        else:
            # Add between 3 and 7 random genres
            self.genres.add(*list(GenreFactory.create_batch(random.randint(3, 7))))
            
def generate_image_base_64():
    # Generate an image with Pillow
    image = Image.new('RGB', (150, 150), color='red')
    buffered = BytesIO()
    image.save(buffered, format='JPEG')
    image_base_64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return f"data:image/jpeg;base64,{image_base_64}"