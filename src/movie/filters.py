import django_filters
from .models import Movie
from django import forms

class MovieFilter(django_filters.FilterSet):
    rate = django_filters.NumberFilter(field_name='rate', lookup_expr='gt')
    
    class Meta:
        model = Movie
        fields = ['type', 'country', 'language', 'released']



class MovieSearch(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains',
                                     widget=forms.TextInput(attrs={'class': 'fa fa-search', 'required': True, 'placeholder': 'Search your Keyword',
                                                                   'name': 'search', 'input_type': 'search',
                                                                   }))
    
    class Meta:
        model = Movie
        fields = []