from django.urls import path
from main.views import show_main, show_list, database_make

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('list-book', show_list, name='show_list'),
    path('SECRET-ONLY/', database_make, name='database_make'),
]