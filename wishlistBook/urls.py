from django.urls import path
from wishlistBook.views import show_wishlist, get_books_json, deleteWishlist, add_wishlist, get_json, add_flutter

app_name = 'wishlistBook'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('get-books-json/<int:book_id>/', get_books_json, name='get_books_json'),
    path('delete/', deleteWishlist, name='deleteWishlist'),
    path('add_wishlist/<int:book_id>/', add_wishlist, name='add_wishlist'),
    path('get-json/', get_json, name='get_json'),
    path('add-flutter/', add_flutter, name='add_fluter'),
]