from django.urls import path
from main.views import show_main
from listBook.views import show_list, show_myBook, get_book, add_book, show_list_filter

app_name = 'listBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('list-book', show_list, name='show_list'),
    path('list-book/list-book-filter/<str:genre>/', show_list_filter, name='show_list_filter'),
    path('my-book', show_myBook, name='show_myBook'),
    path('get-book/', get_book, name='get_book'),
    path('add-book/', add_book, name='add_book')
]