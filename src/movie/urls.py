from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name='movies'),
    path('movie_details/<slug:slug>', views.movie_details, name='movie_details'),
    path('actor/<slug:slug>', views.actor_details, name='actor'),
    path('all', views.all_movies, name="all"),
    path('search', views.searched_movies, name="search"),
    path('type/<slug:slug>', views.movies_in_type, name='type'),
    path('series_details/<slug:slug>', views.series_details, name='series_details'),
    path('season/<slug:slug>', views.show_epsoides, name='season'),
    path('epsoide/<slug:slug>', views.epsoide_details, name='epsoide_details'),
    path('all_series', views.all_series, name='all_series'),
]