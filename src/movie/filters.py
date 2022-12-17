import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    rate = django_filters.NumberFilter(field_name='rate', lookup_expr='gt')
    
    class Meta:
        model = Movie
        fields = ['type', 'country', 'language', 'released']