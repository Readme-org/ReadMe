from django.urls import path
from main.views import show_main
from wishlistBook.views import show_wishlist, get_books_json, deleteWishlist

app_name = 'wishlistBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('wishlist-book', show_wishlist, name='show_wishlist'),
    path('get-books/', get_books_json, name='get_books_json'),
    path('delete-wishlist/', deleteWishlist, name='deleteWishlist'),
]