from django.urls import path
from main.views import show_main, database_make

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('SECRET-ONLY/', database_make, name='database_make'),
]