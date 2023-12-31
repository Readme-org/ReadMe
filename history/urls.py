from django.urls import path
from .views import history, show_history_json
from .views import add_search_history
from .views import history, add_search_history
from . import views

app_name = 'history'

urlpatterns = [
    path('', history, name='history'),
    path('add/', add_search_history, name='add-search-history'),
    path('delete/', views.delete_history_ajax, name='delete_history_ajax'),
    path('history-json/', show_history_json, name='show_history_json'), 
]