from django.urls import path
from main.views import show_main
from wishlistBook.views import show_wishlist

app_name = 'wishlistBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('wishlist-book', show_wishlist, name='show_wishlist'),
]