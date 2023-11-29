from django.urls import path
from main.views import show_main
from wishlistBook.views import show_wishlist, show_wishlist_json

app_name = 'wishlistBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('wishlist-book', show_wishlist, name='show_wishlist'),
    path('wishlist-json/', show_wishlist_json, name='show_wishlist_json'), 
]