from django.urls import path
from main.views import show_main
from listBook.views import add_book_flutter, delete_book_flutter, show_book_json, show_book_title_json, show_list, show_myBook, get_book, add_book, show_list_filter, delete_book, show_list_title, show_mybook_json

app_name = 'listBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('list-book', show_list, name='show_list'),
    path('list-book-filter/<str:genre>/', show_list_filter, name='show_list_filter'),
    path('show_list_title/', show_list_title, name='show_list_title'),
    path('my-book', show_myBook, name='show_myBook'),
    path('get-book/', get_book, name='get_book'),
    path('add-book/', add_book, name='add_book'),
    path('delete-book/<int:id>/', delete_book, name='delete_book'),
    path('myBook-json/', show_mybook_json, name='show_myBook_json'), 
    path('book-json/', show_book_json, name='show_book_json'), 
    path('book-json/<str:title>/', show_book_title_json, name='show_book_title_json'), 
    path('add-book-flutter/', add_book_flutter, name='add_book_flutter'),
    path('delete-book-flutter/<int:id>/', delete_book_flutter, name='delete_book_flutter'),
]
