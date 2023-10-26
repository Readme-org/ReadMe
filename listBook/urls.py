from django.urls import path
from main.views import show_main
from listBook.views import show_list

app_name = 'listBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('list-book', show_list, name='show_list'),
    
]