from django.urls import path
from .views import history
from .views import add_search_history
from .views import history, add_search_history


app_name = 'history'

urlpatterns = [
    path('', history, name='history'),
    path('add/', add_search_history, name='add-search-history'),
]