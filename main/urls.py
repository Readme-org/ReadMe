from django.urls import path
from . import views # Tambah ini
from main.views import show_json, show_main, database_make, register, login_user, logout_user
from main.views import get_book, add_book

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('SECRET-ONLY/', database_make, name='database_make'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_book/', add_book, name='add_book'),
    path('get-book/', get_book, name='get_book'),
    path('json/', show_json, name='show_json'), 
]