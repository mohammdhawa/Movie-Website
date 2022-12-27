from django.shortcuts import render, redirect
from .models import Movie, Actor, MovieType, Series, Season, Epsoide
from .filters import MovieFilter, MovieSearch
from django.urls import reverse
from accounts.forms import CommentForm
from accounts.models import Profile

# Create your views here.

def movies_list(request):
    movies = Movie.objects.all()
    series = Series.objects.all()
    
    lastest_4 = Movie.objects.all().order_by('-id')[:4]
    popular_4 = Movie.objects.all().order_by('rate')[:4]
    lastest_6 = Movie.objects.all().order_by('-id')[:6]
    recent_9 = movies.order_by('-id')[:9]
    popular_9 = movies.order_by('rate')[:9]
    top_3 = movies.order_by('rate')[:3]
    
    context = {'movies': movies, 'movies_4': lastest_4, 
               'popular_4': popular_4, 'lastest_6': lastest_6,
               'series': series, 'recent_9': recent_9, 'popular_9': popular_9,
               'top_3': top_3}
    return render(request, 'movie/movies_list.html', context)


# @login_required(login_url='/accounts/login/')
def movie_details(request, slug):
    movie = Movie.objects.get(slug=slug)
    comments = movie.comment_set.all()
    
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user.id)
            form.instance.movie = movie
            form.instance.user = profile
            form.save()
            return redirect(reverse('movies:movie_details', kwargs={
                'slug': movie.slug
            }))
    
    context = {'movie': movie, 'form': form, 'comments': comments}
    return render(request, 'movie/movie_detail.html', context)


def actor_details(request, slug):
    actor = Actor.objects.get(slug=slug)
    movies = Movie.objects.filter(actors=actor.id)
    
    context = {'actor': actor, 'movies': movies}
    return render(request, 'movie/actor.html', context)


def all_movies(request):
    first_3 = Movie.objects.all().order_by('rate')[0:3]
    second_3 = Movie.objects.all().order_by('rate')[3:6]
    my_popular = zip(first_3, second_3)
    
    all_movies = Movie.objects.all().order_by('-id')
    myfilter = MovieFilter(request.GET, all_movies)
    all_movies = myfilter.qs
    
    context = {'my_popular': my_popular, 'all_movies': all_movies, 'myfilter': myfilter}
    return render(request, 'movie/all_movies.html', context)


def movies_in_type(request, slug):
    type = MovieType.objects.get(slug=slug)
    movies = Movie.objects.filter(type=type.id)
    
    context = {'movies': movies, 'type': type}
    return render(request, 'movie/movies_of_type.html', context)


def series_details(request, slug):
    seri = Series.objects.get(slug=slug)
    seasons = Season.objects.filter(series=seri.id)

    context = {'seri': seri, 'seasons': seasons}
    return render(request, 'movie/series_details.html', context)


def show_epsoides(request, slug):
    season = Season.objects.get(slug=slug)
    epsoides = Epsoide.objects.filter(season=season.id)
    
    context = {'epsoides': epsoides, 'season': season}
    return render(request, 'movie/epsoides.html', context)


def epsoide_details(request, slug):
    epsoide = Epsoide.objects.get(slug=slug)
    
    context = {'epsoide': epsoide}
    return render(request, 'movie/epsoide_details.html', context)


def all_series(request):
    all_series = Series.objects.all().order_by('-id')
    
    print(all_series)
    
    context = {'all_series': all_series}
    return render(request, 'movie/all_series.html', context)


def searched_movies(request):
    
    all_movies = Movie.objects.all().order_by('-id')
    myfilter = MovieSearch(request.GET, all_movies)
    all_movies = myfilter.qs
    
    context = {'all_movies': all_movies, 'myfilter': myfilter}
    return render(request, 'movie/searched_movies.html', context)