from django.urls import path
from wishlistBook.views import show_wishlist, get_books_json, deleteWishlist, add_wishlist

app_name = 'wishlistBook'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('get-books-json/<int:book_id>/', get_books_json, name='get_books_json'),
    path('delete-Wishlist/<int:id>', deleteWishlist, name='deleteWishlist'),
    path('add_wishlist/<int:book_id>/', add_wishlist, name='add_wishlist')
]