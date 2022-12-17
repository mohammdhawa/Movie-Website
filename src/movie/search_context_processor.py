from .models import Movie, MovieType
from .filters import MovieSearch

def search_movies(request):
    all_movies = Movie.objects.all().order_by('-id')
    myfilter = MovieSearch(request.GET, all_movies)
    all_movies = myfilter.qs
    
    all_categories = MovieType.objects.all()
    
    return {'search_form': myfilter, 'searched_movies': all_movies, 'all_categories': all_categories}
    